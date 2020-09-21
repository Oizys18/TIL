    function executeCallbacks() {  
        setTimeout(function () {
            var i;
            for (i = 0; i < 5; i++) {
                (function(){
                    var j = i;
                    setTimeout(function (){
                        console.log('j:'+ j + ', i:'+ i);
                    }, 1000);
                })();
            }
        }, 0);
    }

    console.log('start');
    executeCallbacks();  
    console.log('end');
