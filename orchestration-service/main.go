package main

import (
	"fmt"
	"log"
	"net/http"

	"ai_content_os/orchestration-service/workflows"
)

func main() {
	// TODO: Initialize a new router

	// TODO: Register workflow routes
	http.HandleFunc("/", workflows.HealthCheckHandler)

	// TODO: Start the HTTP server
	fmt.Println("Orchestration Service listening on port 8081")
	log.Fatal(http.ListenAndServe(":8081", nil))
}

/*
// Reference Implementation
package main

import (
	"fmt"
	"log"
	"net/http"

	"ai_content_os/orchestration-service/workflows"
	"github.com/gorilla/mux"
)

func main() {
	r := mux.NewRouter()

	workflows.RegisterRoutes(r)

	fmt.Println("Orchestration Service listening on port 8081")
	log.Fatal(http.ListenAndServe(":8081", r))
}
*/
