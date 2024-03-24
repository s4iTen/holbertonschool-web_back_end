export default class Pricing {
    constructor(amount, currency) {
      this._amount = amount;
      this._currency = currency;
    }
  
    get amount() {
      return this._amount;
    }
  
    get currency() {
      return this._currency;
    }
  
    set amount(value) {
      this._amount = value;
    }
  
    set currency(value) {
      this._currency = value;
    }
  
    displayFullPrice() {
      return `${this.amount} ${this.currency.displayFullCurrency()}`;
    }
  
    static convertPrice(amount, conversionRate) {
      return amount * conversionRate;
    }
  }