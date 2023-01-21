function calculate() {
    var loanAmount = document.getElementById("loan-amount").value;
    var interestRate = document.getElementById("interest-rate").value;
    var loanTerm = document.getElementById("loan-term").value;
    // perform calculations here (example calculation is for demonstration purposes only)
    var monthlyPayment = (loanAmount * interestRate) / (12 * (1 - Math.pow(1 + interestRate, -loanTerm)));

    // output the results to the "output" element
    var output = document.getElementById("output");
    output.innerHTML = "Monthly Payment: $" + monthlyPayment;
}