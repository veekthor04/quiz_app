function countdown( elementName, minutes, seconds ) {
    var element, endTime, hours, mins, msLeft, time;

    function twoDigits( n ) {
        return (n <= 9 ? "0" + n : n);
    }

    function updateTimer() {
        msLeft = endTime - (+new Date);
        if ( msLeft < 1000 ) {
            alert("Time is up!");
            document.getElementById("quiz").submit();
        } else {
            time = new Date( msLeft );
            hours = time.getUTCHours();
            mins = time.getUTCMinutes();
            element.innerHTML = (hours ? hours + ':' + twoDigits( mins ) : mins) + ':' + twoDigits( time.getUTCSeconds() );
            setTimeout( updateTimer, time.getUTCMilliseconds() + 500 );
        }
    }

    element = document.getElementById( elementName );
    endTime = (+new Date) + 1000 * (60*minutes + seconds) + 500;
    updateTimer();
}

if (document.getElementById("quiz")){
    countdown( "time", time_minute, time_second );

    document.querySelectorAll('.submit_quiz').forEach(item => {
        item.addEventListener('click', event => {
            var choice = confirm("Are you sure you want to submit the quiz!")
            if (choice == true) {
                document.getElementById('quiz').submit();
            }
        })
      })

    // document.addEventListener("mouseleave", function(event){

    //     if(event.clientY <= 0 || event.clientX <= 0 || (event.clientX >= window.innerWidth || event.clientY >= window.innerHeight))
    //     {
      
    //     //    alert("Do not leave the window")
           
    //     //    document.getElementById("quiz").submit();

    //     console.log('left');

    //     setTimeout(function(){ 
            
    //     if(event.clientY <= 0 || event.clientX <= 0 || (event.clientX >= window.innerWidth || event.clientY >= window.innerHeight))
    //     {
    //             console.log('close');
            
    //         }
    //     }, 3000);
        
      
    //     }
    // });

}



// const mouseTarget = document.getElementById("wrapper");

// mouseTarget.addEventListener('mouseleave', e => {
//     console.log('left');
//     setTimeout(function(){ 
//         mouseTarget.addEventListener('mouseleave', e => {
//             console.log('close');
        
//         });
//      }, 3000);

// });

// mouseTarget.addEventListener('mouseenter', e => {

//     console.log('enter');

// });





