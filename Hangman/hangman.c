//array of words 
//length of word == the amount of lines showing
//user enters different letters to match the letters in word
//correct guessed letters get replaced in dashes 
//create actual hangman when answers are guessed wrong and if the whole man is made the game ends
//hangman contents - head, one arm, other arm, one leg, other leg, body 

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

void update(int count){
    if (count == 0){
        printf("  -----\n");
        printf("  |\n");
        printf("  |\n");
        printf("  |\n");
        printf("  |\n");
        printf("  |\n");
        printf("_____\n");
    }
    if (count == 1){
        printf("  -----\n");
        printf("  |     |\n");
        printf("  |     O\n");
        printf("  |\n");
        printf("  |\n");
        printf("  |\n");
        printf("_____\n");
    }
    if (count == 2){
        printf("  -----\n");
        printf("  |     |\n");
        printf("  |     O\n");
        printf("  |     |\n");
        printf("  |\n");
        printf("  |\n");
        printf("_____\n");
    }
    if (count == 3){
        printf("  -----\n");
        printf("  |     |\n");
        printf("  |     O\n");
        printf("  |    /|\n");
        printf("  |\n");
        printf("  |\n");
        printf("_____\n");
    }
    if (count == 4){
        printf("  -----\n");
        printf("  |     |\n");
        printf("  |     O\n");
        printf("  |    /|\\\n");
        printf("  |\n");
        printf("  |\n");
        printf("_____\n");
    }
    if (count == 5){
        printf("  -----\n");
        printf("  |     |\n");
        printf("  |     O\n");
        printf("  |    /|\\\n");
        printf("  |    /\n");
        printf("  |\n");
        printf("_____\n");
    }
    if (count == 6){
        printf("  -----\n");
        printf("  |     |\n");
        printf("  |     O\n");
        printf("  |    /|\\\n");
        printf("  |    / \\\n");
        printf("  |\n");
        printf("_____\n");
    }
    
}
int main(){
    const char *a[5] = {"apple", "service", "chocolate", "pen", "toast"};
    const char *random;
    srand(time(NULL));
    random = a[rand() % 5];
    int length = strlen(random);
    

    int counter = length;
    printf("  ");
    for (int i=1; i<=counter;i++){
        printf("_");
    }
    printf("\n");
    for (int a = 1; a<=counter; a++){
        printf("  |"); 
        printf("\n");
    }
    for (int i=1; i<=counter;i++){
        printf("_");
    }
    char dash[100];
    printf("\n");
    for (int i=0; i<length;i++){
        dash[i] = '_';
        
    }
    dash[length] = '\0';
    printf("%s\n", dash);
    printf("\n");
    
    char guess; //stores guessed letters 
    int ans = 0;
    int count = 0;
    
    while ((ans!=length) && (count != 6)){
        int correct = 0;
       
        printf("Enter a guess from a-z: ");
        scanf(" %c", &guess);
        

        for(int i=0; i<length;i++){
            if (guess == random[i]){
                correct = 1;
                ans++;
                if (dash[i] == '_'){
                    dash[i] = guess;
                }
            } 
        }
        if (correct == 0){
            count++;
        }
        update(count);
        printf("%s\n", dash);
        if (correct){
            printf("You Guessed Correctly\n");
        }else{
            printf("You Guessed Incorrectly\n");
        }

    }

    if (count == 6){
        printf("Game Over! The word was %s.\n", random);
    } else {
        printf("Congratulations! You won!\n");
    }

    return 0;
}



