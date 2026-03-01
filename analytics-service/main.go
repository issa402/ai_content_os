package main

import (
	"fmt"
	"log"
	"net/http"

	"ai_content_os/analytics-service/collectors"
)

func main() {
	// TODO: Initialize a new router

	// TODO: Register analytics routes
	http.HandleFunc("/", collectors.HealthCheckHandler)

	// TODO: Start the HTTP server
	fmt.Println("Analytics Service listening on port 8085")
	log.Fatal(http.ListenAndServe(":8085", nil))
}

/*
// Reference Implementation
package main

import (
	"fmt"
	"log"
	"net/http"

	"ai_content_os/analytics-service/collectors"
	"github.com/gorilla/mux"
)

func main() {
	r := mux.NewRouter()

	collectors.RegisterRoutes(r)

	fmt.Println("Analytics Service listening on port 8085")
	log.Fatal(http.ListenAndServe(":8085", r))
}
*/
