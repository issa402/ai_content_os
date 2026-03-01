package main

import (
	"fmt"
	"log"
	"net/http"

	"ai_content_os/api-gateway/handlers"
)

func main() {
	// TODO: Initialize a new router

	// TODO: Register API routes
	http.HandleFunc("/", handlers.HealthCheckHandler)

	// TODO: Start the HTTP server
	fmt.Println("API Gateway listening on port 8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}

/*
// Reference Implementation
package main

import (
	"fmt"
	"log"
	"net/http"

	"ai_content_os/api-gateway/handlers"
	"github.com/gorilla/mux"
)

func main() {
	r := mux.NewRouter()

	handers.RegisterRoutes(r)

	fmt.Println("API Gateway listening on port 8080")
	log.Fatal(http.ListenAndServe(":8080", r))
}
*/
