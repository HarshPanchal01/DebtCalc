function calculate() {
    console.log("Calculating...");
    var loanAmount = document.getElementById("loan-amount").value;
    console.log("loanAmount: ", loanAmount);
    var interestRate = document.getElementById("interest-rate").value;
    console.log("interestRate: ", interestRate);
    var loanTerm = document.getElementById("loan-term").value;
    console.log("loanTerm: ", loanTerm);

    if(loanAmount == "" || interestRate == "" || loanTerm == "") {
        document.getElementById("output").innerHTML = "Please enter valid values for loan amount, interest rate, and loan term";
        return;
    }

    if(isNaN(loanAmount) || isNaN(interestRate) || isNaN(loanTerm)) {
        document.getElementById("output").innerHTML = "Please enter valid values for loan amount, interest rate, and loan term";
        return;
    }
    var monthlyInterestRate = (interestRate / 100) / 12;
    var monthlyPayment = loanAmount * monthlyInterestRate / (1 - Math.pow(1 + monthlyInterestRate, -loanTerm * 12));
    var totalInterest = (monthlyPayment * loanTerm * 12) - loanAmount;
    var totalAmount = totalInterest + loanAmount;
    if (isNaN(monthlyPayment) || monthlyPayment === Infinity) {
              document.getElementById("output").innerHTML = "Please enter valid values for loan amount, interest rate, and loan term";
    } else {
      document.getElementById("output").innerHTML = "Monthly Payment: $" + monthlyPayment.toFixed(2) + "<br>" + "Total Interest: $" + totalInterest.toFixed(2) + "<br>" + "Total Amount: $" + totalAmount.toFixed(2);
    }
}
     
