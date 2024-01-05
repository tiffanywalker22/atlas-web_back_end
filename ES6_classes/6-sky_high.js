import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, flors) {
    super(sqft);
    this._floors = floors;
  }

  get sqft() {
    return this._floors;
  }

  get floors() {
    return this._floors;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this.floors} floors`;
  }
}
