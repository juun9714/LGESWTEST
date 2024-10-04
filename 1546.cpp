#include <iostream>
#include <vector>
#include <algorithm>

int main(void){
    double N=0, tmpScore=0, sum=0;
    std::vector<double> scores;

    std::cin>>N;

    for(int i=0; i<N; i++){
        std::cin>>tmpScore;
        scores.push_back(tmpScore);
    }
    int M=*max_element(scores.begin(), scores.end());

    //점수/M*100으로 고쳤다.

    for(auto score: scores){
        sum+=score;
    }
    sum=sum/(double)M*100;

    std::cout<<sum/N<<std::endl;

    return 0;
}