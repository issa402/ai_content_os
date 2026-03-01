package main

import (
	"fmt"
	"log"
	"net/http"

	"ai_content_os/ingestion-service/ingesters"
)

func main() {
	// TODO: Initialize a new router

	// TODO: Register ingestion routes
	http.HandleFunc("/", ingesters.HealthCheckHandler)

	// TODO: Start the HTTP server
	fmt.Println("Ingestion Service listening on port 8082")
	log.Fatal(http.ListenAndServe(":8082", nil))
}

/*
// Reference Implementation
package main

import (
	"fmt"
	"log"
	"net/http"

	"ai_content_os/ingestion-service/ingesters"
	"github.com/gorilla/mux"
)

func main() {
	r := mux.NewRouter()

	ingesters.RegisterRoutes(r)

	fmt.Println("Ingestion Service listening on port 8082")
	log.Fatal(http.ListenAndServe(":8082", r))
}
*/
