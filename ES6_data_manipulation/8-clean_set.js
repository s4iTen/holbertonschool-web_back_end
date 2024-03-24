const cleanSet = (set, startString) => {
    if (typeof set !== 'object' || typeof startString !== 'string' || startString.length === 0) {
      return '';
    }
  
    const result = [];
    for (const element of set) {
      if (element && typeof element === 'string' && element.startsWith(startString)) {
        result.push(element.slice(startString.length));
      }
    }
    return result.join('-');
  };
  
  export default cleanSet;