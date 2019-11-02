switch("computer wins!") {
    case "computer wins!":
        return " HAHA DUMB ASS\, I\'M JUST FEW LINES OF CODES AND YOU CAN\'T EVEN BEAT ME! SHAME ON YOU ";
    case "user wins!":
        return " YOU CREATED ME\, FATHER. DON\'T GET TOO EXCITED.";
    default: "WE HAVE THE SAME LEVEL OF INTELIGENCE\, RIGHT?";
}
    

var userChoice = prompt("Do you choose rock, paper or scissors?");
var computerChoice = Math.random();
if (computerChoice < 0.34) {
	computerChoice = "rock";
} else if(computerChoice <= 0.67) {
	computerChoice = "paper";
} else {
	computerChoice = "scissors";
} 

var compare = function (choice1, choice2) {
    if (choice1 === choice2) {
        return "The result is a tie!";
//choice1 = rock
    } else if (choice1 === "rock") {
        if(choice2 === "scissors") {
            return "user wins!";
        } else {
            return "computer wins!";
        }
//choice1 = paper       
    } else if (choice1 === "paper") {
        if(choice2 === "rock") {
            return "user wins!";
        } else {
            return "computer wins!";
        }
//choice1 = rock
    } else if (choice1 === 'scissors') {
        if(choice2 === "rock") {
            return "computer wins!";
        } else {
            return "user wins!";
        }       
  }
};
