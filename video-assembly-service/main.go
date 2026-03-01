package main

import (
	"fmt"
	"log"
	"net/http"

	"ai_content_os/video-assembly-service/assemblers"
)

func main() {
	// TODO: Initialize a new router

	// TODO: Register assembly routes
	http.HandleFunc("/", assemblers.HealthCheckHandler)

	// TODO: Start the HTTP server
	fmt.Println("Video Assembly Service listening on port 8083")
	log.Fatal(http.ListenAndServe(":8083", nil))
}

/*
// Reference Implementation
package main

import (
	"fmt"
	"log"
	"net/http"

	"ai_content_os/video-assembly-service/assemblers"
	"github.com/gorilla/mux"
)

func main() {
	r := mux.NewRouter()

	assemblers.RegisterRoutes(r)

	fmt.Println("Video Assembly Service listening on port 8083")
	log.Fatal(http.ListenAndServe(":8083", r))
}
*/
