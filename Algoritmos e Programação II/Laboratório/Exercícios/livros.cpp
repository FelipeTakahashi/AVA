#include <stdio.h>
#define MAXSIZE 10
#define MAXL 30

using namespace std;

struct Library {
	char Title[MAXL+1];
	char Author[MAXL+1];
	int Year;
}books[MAXSIZE];

void setBooks(Library books[MAXSIZE], int n) {
	for (int i = 0; i < n; ++i) {
		printf("\nTitle: ");
		scanf("%s", books[i].Title);
		printf("\nAuthor: ");
		scanf("%s", books[i].Author);
		printf("\nYear: ");
		scanf("%d", &books[i].Year);
	}
	return;
}

void getBooksBeforeYear(Library books[MAXSIZE], int n, int year) {
	int counter = 0;
	for (int i = 0; i < n; i++) {
		if (books[i].Year < year) {
			printf("\nBook %d\nTitle: %s\nAuthor: %s\nYear: %d\n\n", ++counter, books[i].Title, books[i].Author, books[i].Year);
		}
	}
	return;
}

int main() {
	int n;
	printf("Number of books to be registered: ");
	scanf("%d", &n);
	
	setBooks(books, n);
	
	int year;
	printf("\nSearch books before year: ");
	scanf("%d", &year);
	
	getBooksBeforeYear(books, n, year);
	
	return 0;
}
