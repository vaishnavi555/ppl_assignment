#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
int sec = 0;
int min = 0;
int hrs = -01;
pthread_mutex_t mutex1 = PTHREAD_MUTEX_INITIALIZER;

void *hours(void *vargp) {

	if(hrs == -01 || min == 5) {
		pthread_mutex_lock(&mutex1);
		hrs = hrs + 1;
		min = 0;
		sec = 0;
		pthread_mutex_unlock(&mutex1);
	}
	return NULL;
}

void *minutes(void *vargp) {

	if(min <= 05) {
		pthread_mutex_lock(&mutex1);
		sleep(1);
		min = min + 1;
		sec = 0;
		pthread_mutex_unlock(&mutex1);
	}
	return NULL;
}

void *seconds(void *vargp) {

	while(sec != 5) {
		pthread_mutex_lock(&mutex1);
		sleep(1);
		printf("\n%d",hrs);
		printf(":%d",min);
		printf(":%d",sec);
		sec = sec + 1;
		pthread_mutex_unlock(&mutex1);
	}
	return NULL;
}

int main() {
	pthread_t thread_id1, thread_id2, thread_id3;
	printf("CLOCK STARTS NOW!");
	while(1) {
		pthread_create(&thread_id1,NULL,hours,NULL);
		sleep(1);
		pthread_create(&thread_id3,NULL,seconds,NULL);
		sleep(1);
		pthread_create(&thread_id2,NULL,minutes,NULL);
		sleep(1);
		pthread_join(thread_id1,NULL);
		pthread_join(thread_id3,NULL);
		pthread_join(thread_id2,NULL);
	}
	return 0;

}

