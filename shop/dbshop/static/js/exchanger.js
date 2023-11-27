async function exchange(money, currency) {
    const response = await fetch('https://v6.exchangerate-api.com/v6/bb1cc5a13cc79aade21b246b/latest/USD');
    const data = await response.json();
    const exchangedMoney = money * data.conversion_rates[currency];
    return `${exchangedMoney.toFixed(2)} ${currency}`;
}

function performExchange() {
    const currencySelect = document.getElementById('currency');
    const moneyAmountInput = parseFloat(document.getElementById('moneyAmount').dataset.goodPrice);
    const resultDiv = document.getElementById('result');

    if (!currencySelect) {
        console.error("CurrencySelect not found");
        return;
    }

    if (!moneyAmountInput) {
        console.error("MoneyAmount not found!");
        return;
    }

    if (!resultDiv) {
        console.error("ResultDiv not found!");
        return;
    }

    if (isNaN(moneyAmountInput)) {
        console.error("MoneyAmount is NaN")
    }

    const moneyAmount = parseFloat(moneyAmountInput.value);
    const targetCurrency = currencySelect.value;

    exchange(moneyAmountInput, targetCurrency)
        .then(result => {
            resultDiv.innerText = `Costs ${result}`;
        })
        .catch(error => console.error(error));
}

document.addEventListener('DOMContentLoaded', performExchange);