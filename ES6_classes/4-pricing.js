import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  set amount(amount) {
    if (typeof amount !== 'number') {
      throw new TypeError('amount must be a number');
    } else {
      this._amount = amount;
    }
  }

  get amount() {
    return this._amount;
  }

  set currency(currency) {
    if (!(currency instanceof Currency)) {
      throw new Error('currency is not an instance of Currency');
    } else {
      this._currency = currency;
    }
  }

  get currency() {
    return this._currency;
  }

  displayFullPrice() {
    return `${this._name} (${this._code})`;
  }

  convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
