// Note: Requires POSIX sockets, simplified skeleton
#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

int main() {
    int sock;
    struct sockaddr_in server;
    char message[1024], server_reply[2000];
    
    sock = socket(AF_INET, SOCK_STREAM, 0);
    server.sin_addr.s_addr = inet_addr("93.184.216.34"); // example.com IP
    server.sin_family = AF_INET;
    server.sin_port = htons(80);

    connect(sock, (struct sockaddr *)&server, sizeof(server));
    strcpy(message, "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n");
    send(sock, message, strlen(message), 0);
    recv(sock, server_reply, sizeof(server_reply)-1, 0);
    printf("%s\n", server_reply);
    close(sock);
    return 0;
}
