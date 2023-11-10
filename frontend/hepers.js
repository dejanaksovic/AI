//Path between two points
export
const moveOnLine = (x1, y1, x2, y2, speed) => {
    // Formula
    // y-y1 = (y2-y1)/(x2-x1)(x-x1)
   const points = [];
   //Racunamo putanju
   for(let x = x1; x <= x2; x += speed) {
      let y = (y2-y1) / (x2-x1) * (x-x1) + y1;
      points.push([x, y]);
   }

   return points;
}