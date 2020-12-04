const done = false; 
const toDos = []

while(true){

    let action = prompt("Choose an option");

   if(action ==='quit'){
       break;
   }
   else if(action ==="new"){
      newToDo = prompt("What do you wanna add");
      toDos.push(newToDo);

   }
   else if (action ==="list") {

       console.log("*************");
       for(let i =0 ; i<=toDos.length-1; i++){
           console.log(`${i}: ${toDos[i]}`)
       }
       console.log("*************");

   }
   else if (action ==="delete") {
       rmIndex = prompt("What would you wanna Delete Fam")
       toDos.splice(rmIndex,1)

   }

}



