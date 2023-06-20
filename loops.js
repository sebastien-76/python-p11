// Boucle for classique
for (let i = 0; i < 10; i++) {
console.log("i = " + i);
}

//Boucle à rebours
for (let i = 10; i >0; i--) {
    console.log("i = " + i);
    }

// Boucle for each
// le mot clé of permet de récupérer l'élément
let users = ['foo', 'bar', 'baz']
//le mot of recupère l'élément        
for (let user of users ) {
    console.log(user)
}

//le mot in recupère l'index de l'élément    
for (let user in users ) {
    console.log(user)
}

for (let i in users) {
    let user =users[i];
    console.log(`i = ${i}, user = ${users[i]}`);
}

//syntaxe alternative
users.forEach(
    (user, i, list) => {
        console.log(`i = ${i}, user = ${user}`);    
    }
);

users.forEach(
    function(user, i, list){
        console.log(`i = ${i}, user = ${user}`);    
    }
);