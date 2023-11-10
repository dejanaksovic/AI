//imports
import { moveOnLine } from "./hepers";

// Ui and init
const sampleMap = [
   [94, 485],
   [150, 149, 7],
   [438, 410, 6],
   [745, 540, 10],
   [823, 231, 10],
]
// Za ulazenje u mod korak po korak
let state = "single"
// Tezi put == sporije kretanje, laksi - brze
let speed = 1;

// Move a step
let currentStep = 0;
const moveStep = (back) => {
   if(back) {
      if(currentStep === 0) 
         return
      currentStep --
   }
   const x1 = sampleMap[currentStep][0];
   const y1 = sampleMap[currentStep][1];
   const x2 = sampleMap[currentStep+1][0];
   const y2 = sampleMap[currentStep+1][1];
   const steps = moveOnLine(x1, y1, x2, y2, speed);
   if(back) {
      steps.reverse();
   }
   else {
   currentStep = (currentStep+1)%sampleMap.length;
   }
   player.addMovePath(steps);
   console.log(currentStep);
}

window.addEventListener('keydown', e => {
   if(state === "single") {
      if(e.key === "ArrowRight")
         moveStep();
      else if(e.key === "ArrowLeft") {
         moveStep(true);
      }
   }
})

// GAME
// init setup
const canvas = document.querySelector('canvas');
document.body.style.backgroundColor = "black";
canvas.width = 900;
canvas.height = 600;
const ctx = canvas.getContext('2d');

class gameObject {
   static objects = [];
   constructor() {
      gameObject.objects.push(this);
   }
}

class Sprite {
   constructor(x, y, imgSrc, width, height) {
      this.x = x;
      this.y = y;
      this.img = new Image();
      this.img.src = imgSrc;
      this.width = width;
      this.height = height;
   }

   draw() {
      if(!this.img) {
         return new Error('Sprite has no image to fallback to');
      }
      if(this.width && this.height)
         return ctx.drawImage(this.img, this.x, this.y, this.width, this.height);
      ctx.drawImage(this.img, this.x, this.y);
   }

}

class Player extends gameObject {
   constructor (x, y) {
      super();
      this.sprite = new Sprite(x, y, '/assets/sprites/Aki.png', 50, 50);
   }

   addMovePath(movePath) {
      this.movePath = movePath;
      this.step = 0;
   }

   onUpdate() {
      if(this.movePath) {
         this.sprite.x = this.movePath[this.step][0];
         this.sprite.y = this.movePath[this.step++][1];
         if(this.step >= this.movePath.length) {
            this.step = null;
            this.movePath = null;
         }
      }
      this.sprite.draw();
   }

}

class Background extends gameObject {
   constructor(x, y) {
      super();
      this.sprite = new Sprite(x, y, '/assets/maps/terrain.png');
   }

   onUpdate() {
      this.sprite.draw();
   }
}

class Coin extends gameObject {
   constructor(x, y, player) {
      super();
      this.sprite = new Sprite(x, y, '/assets/sprites/coin.png', 50, 50);
      this.isPickedUp = false;
      this.player = player;
   }

   onUpdate() {
      if(this.player.sprite.x === this.sprite.x && this.player.sprite.y === this.sprite.y) {
         this.isPickedUp = true;
         this.sprite.img.src = 'assets/sprites/collected_coin.png';
      }
      this.sprite.draw();
   }
}

// Initial map state
const background = new Background(0, 0);
const player = new Player(sampleMap[0][0], sampleMap[0][1]);
//initing coins
sampleMap.forEach(([i, j, k]) => {
   if(!k)
      return
   const coin = new Coin(i, j, player);
   console.log(gameObject.objects)
})

const animate = () => {
   requestAnimationFrame(animate);
   gameObject.objects.forEach( e => {
      e.onUpdate();
   })
}

animate();

