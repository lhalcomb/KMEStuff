/* Illustrated & Created by Layden E. Halcomb 
  Date: 03/05/2024 
  
  
  ReadME___:
  This was created for developing a visual of the GoldBach Comet from the GoldBach Conjecture. 
  I have zero intentions of solving this infamous conjecture but I do indeed find it very fascinating and enjoy the mathematical joy that it gives me. 
  Maybe this will end up developing into a fractal. But in the mean time, enjoy a very nice picture of a comet displaying over a dark night. 
  
  
  Modification Log:
  03/05/2024 - Began simple development of the set up of calculating the primes using the algorithm given below.
  
*/


int[] primes; //Array to store the primes from the calculate prime function below
int n;


void setup(){
  size(2560, 720); // width = 600 height = 400
  calculatePrimes(100000);
  drawComet();
}

/*
  
*/
void drawComet(){
    background(0); //black
    //translate(0, height/2);
    scale(1.0);
    
    for (int i = 4; i <= width; i+=2){
        int count = countPrimePairs(i);
        float x = map(i, 4, width, 0, width);
        float y = map(count, 0, 100, height, 0);
        fill(255 - pow(count, 2) , pow(count, 2) , 255);
        ellipse(x, y, 3, 3);
    }
}
/* Calculates the Prime Numbers up to the limit n 
  This function uses an ancient algorithm for finding all of the prime numbers up to a given limit. 
  It is known as the Sieve of Eratosthenes. 
  Wikipedia Link to it: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
*/
void calculatePrimes(int n){
   
  boolean[] isPrime = new boolean[n + 1]; //Initialized boolean array to keep track of the prime values. This will be updated during calculation
  
  for(int i = 0; i <= n; i++){
    isPrime[i] = true; //populate the entire isPrime boolean array as true initially 
  }
  
  for (int p = 2; p * p <= n; p++){
    
    //if prime[p] is still true, then it is prime
    if(isPrime[p]){
      for(int i = p * p; i <= n; i += p){
        isPrime[i] = false; //here is where we update all of the multiples of p greater than or equal to the sqaure of its numbers which are multiples of p and are less than p^2 and mark the multiples as non-prime. aka isPrime[p] = false
      }
    }
  }
  
  //count the numbers of those primes for the sake of counting the prime pairs. We need this as an essential "mouseka-tool" for representing a sum as two primes (generating the comet)
  int count = 0;
  for (int i = 2; i <= n; i++){
    if (isPrime[i]){
      count++;
    }
  }
  
  //Then we store those primes. Makes this easier to iterate over when getting those prime pairs
  primes = new int[count];
  int index = 0;
  for (int i = 2; i <= n; i++){
    if (isPrime[i]){
      primes[index++] = i;
    }
  }
}

/* Now we need a function for calculating the number of prime pairs that sum up to the given even number 'n'. */
int countPrimePairs(int n){
  int count = 0;
  for (int i = 2; primes[i] <= n / 2; i++){ //iterates over each prime to n/2. This is because we are interested in prime numbers that sum up to an even n and the largest number that can be such pair is n/2
    if (isPrime(n - primes[i])){ //this checks to make sure that if the difference is prime then we have found exactly what is mentioned above. In other words, (n = even number, primes[i] = prime number, the difference of such should be prime too bc of subtraction and addition)
      count++;
    }
  }
  
  return count;
}

/* Now we develop the isPrime boolean function.
  Description:
    This function determines whether a given integer 'n' is a prime number 
    by checking for divisors from 2 up to the square root of 'n'.
    If 'n' is divisible by any number within this range, 
    it is not prime; else, it is prime.
*/

boolean isPrime(int n){
  if (n <= 1) {
    return false;
  }
  
    for (int i = 2; i * i <= n; i++){
      if (n % i == 0){
        return false;
    }
  }
  return true;

}
