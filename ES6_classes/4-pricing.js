import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this.amount = amount; // number
    this.currency = currency; //currency
  }

  // Setter for amount
  set amount(amount) {
    if (typeof amount !== 'number') {
      throw new TypeError('amount must be a number');
    }
    this._amount = amount;
  }

  // Getter for amount
  get amount() {
    return this._amount;
  }

  // Setter for currency
  set currency(currency) {
    if (typeof currency !== 'currency') {
      throw new TypeError('currency must be a currency code');
    }
    this._currency = currency;
  }

  // Getter for currency
  get currency() {
    return this._currency;
  }

  displayFullPrice(amount, name, code) {
    return `${amount} ${name} (${code})`;
  }

  convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}