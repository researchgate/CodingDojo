package main

import (
	"fmt"
	"math/rand"
	"net/http"
	"strconv"
	"strings"
)

func main() {
	fmt.Println("Initializing.")

	testPattern := "50-1010101010101010\n"

	fmt.Println("Sending test pattern...")

	send(testPattern)

	fmt.Println("Test pattern was sent successfully.")

	message := generate()

	fmt.Println("Sending pattern... ", message)

	send(message)

	fmt.Println("Done.")
}

func send(message string) error {
	body := strings.NewReader(message)

	resp, err := http.Post("http://192.168.178.134:8080", "text/plain", body)

	if err != nil {
		fmt.Println("Message failed to be transmitted, terminating.")
		fmt.Println("Reason:", err)

		return err
	}

	resp.Body.Close()

	return nil
}

func generate() string {
	message := ""

	frameDuration := ""

	empty := "0000"
	filled := "0000"

	for drop := 0; drop < 10; drop += 1 {
		var duration int64 = 150 + rand.Int63n(50)
		frameDuration = strconv.FormatInt(duration, 10) + "-"
		dropPosition := rand.Intn(4)
		filled = ""

		for pixel := 0; pixel < 4; pixel += 1 {
			if pixel == dropPosition {
				filled += "1"
			} else {
				filled += "0"
			}
		}

		for frame := 0; frame < 4; frame += 1 {
			message += frameDuration

			for line := 0; line < 4; line += 1 {
				if line == frame {
					message += filled
				} else {
					message += empty
				}
			}

			message += "\n"
		}
	}

	return message
}
