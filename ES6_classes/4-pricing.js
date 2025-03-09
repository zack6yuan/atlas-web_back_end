import Currency from './3-Currency';

export default class Pricing {
  constructor(amount, currency) {
    this.amount = amount;
    this.currency = currency;
  }

  set amount(amount) {
    if (typeof amount != 'number') {
      throw new TypeError('amount must be a number');
    } else {
      return this.amount;
    }
  }

  get amount() {
    return this.amount;
  }

  set currency(currency) {
    if (currency instanceof Currency) {
      this._currency = currency;
    }
  }

  get currency() {
    return this._currency;
  }

  displayFullPrice(amount, currency) {
    return ``
  }

  convertPrice(amount, conversionRate) {
    return (amount * conversionRate);
  }
}