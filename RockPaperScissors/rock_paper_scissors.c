//randomly selected from computer vs player(user)
//numbers 1, 2, 3 represent rock paper scissors respectively 
//user will type their turn by writing rock paper or scissors 
//computer will generate random number from 1-3 for his turn to see who wins 
//rock kills scissor, paper kills rock, scissors kill paper - if statements 
//game ends when either computer or user has won 3 games - while loop 

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>


int main(){
    srand(time(NULL)); //initialize rand 
    
    char word[20];
    char c;
    int i=0;
    int score_computer = 0; 
    int score_user = 0;
    while (score_computer < 3 && score_user < 3){
        int s = (rand() % 3) + 1; //generate numbers 1-3 to indicate rock, paper, or scissors
        printf("Enter Rock, Paper or Scissors: ");
    
        while ((c = getchar()) != '\n' && i < 19){
            word[i++] = c;
        }
        word[i] = '\0';
        

       if (strcmp(word, "rock") == 0){
            if (s == 1){
                printf("Computer played rock too. Play again\n");
            }else if (s == 2){
                printf("You lost, computer played paper\n");
                score_computer++;
            }else if (s == 3){
                printf("You won, computer played scissors\n");
                score_user++;
            }
       }else if (strcmp(word, "paper") == 0){
            if (s == 1){
                printf("You won, computer played rock\n");
                score_user++;
            }else if (s == 2){
                printf("Computer played paper too. Play again\n");
            }else if (s == 3){
                printf("You lost, computer played scissors\n");
                score_computer++;
            }
       }else if (strcmp(word, "scissors") == 0){
            if (s == 1){
                printf("You lost, computer played rock\n");
                score_computer++;
            }else if (s == 2){
                printf("You won, computer played paper\n");
                score_user++;
            }else if (s == 3){
                printf("Computer played scissors too. Play again\n");
            }

         }

        printf("Computer: %d You: %d\n", score_computer, score_user);
        i = 0;
    }

    if (score_computer < score_user){
        printf("You beat the computer. Congratulations\n");
    } else{
        printf("You have been defeated by the computer\n");
    }

    return 0;
}