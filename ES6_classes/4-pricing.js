import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this.amount = amount; // number
    this.currency = currency; // currency
  }

  set sqft(sqft) {
    if (typeof sqft !== 'number') {
      throw new TypeError('sqft must be a number');
    }
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
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
