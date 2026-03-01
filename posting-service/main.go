package main

import (
	"fmt"
	"log"
	"net/http"

	"ai_content_os/posting-service/posters"
)

func main() {
	// TODO: Initialize a new router

	// TODO: Register posting routes
	http.HandleFunc("/", posters.HealthCheckHandler)

	// TODO: Start the HTTP server
	fmt.Println("Posting Service listening on port 8084")
	log.Fatal(http.ListenAndServe(":8084", nil))
}

/*
// Reference Implementation
package main

import (
	"fmt"
	"log"
	"net/http"

	"ai_content_os/posting-service/posters"
	"github.com/gorilla/mux"
)

func main() {
	r := mux.NewRouter()

	posters.RegisterRoutes(r)

	fmt.Println("Posting Service listening on port 8084")
	log.Fatal(http.ListenAndServe(":8084", r))
}
*/
