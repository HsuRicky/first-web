//console.log("HI")

let example = [1,2,3,5,8,11,19,30,49,79,128]

//console.log( typeof example )

//console.log( typeof 5 )

//console.log( typeof true )


/*
example.forEach((item)=>{
    console.log(item)
    console.log( typeof item )
    //console.log( typeof x )
})
*/

/*
let odd = [] , even = []
example.forEach((item)=>{
    if(item%2==0) even.push(item);
    else odd.push(item)
})
console.log( "odd:",odd )
console.log( "even:",even )
*/

/*
function multiply(a,b,c){
    return a*b*c
}
console.log( multiply(1,2,3) )
*/

let multiply_other = (a) => (b,c) =>{
    return a * (b + c)
}
console.log( multiply_other(10)(3,8) )
console.log( typeof multiply_other)