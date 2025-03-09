import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this.amount = amount; // number
    this.currency = currency; // currency
  }

  set amount(amount) {
    if (amount instanceof amount) {
      this._amount = amount;
    } else {
      throw new TypeError('amount must be a number');
    }
  }

  get amount() {
    return this._currency;
  }

  set currency(currency) {
    if (currency instanceof Currency) {
      this._currency = currency;
    } else {
      throw new TypeError('currency must be a code');
    }
  }

  get currency() {
    return this._currency;
  }

  displayFullPrice() {
    return(`${this._amount} ${this._currency}`)
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
