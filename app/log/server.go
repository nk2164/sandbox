package log

import (stlog "log")

// ServerLogger is a logger for the server
var log *stlog.Logger

type fileLog string

func (f fileLog) Write(data []byte) (n int, err error) {
	f, err := os.OpenFile(string(f), os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0600)
	if err != nil {
		return 0, err
	}
	defer f.Close()
	return f.Write(data)
}

func Run(destination string) {
	log = stlog.New(fileLog(destination), "", stlog.LstdFlags)
}

func RegisterHandlers() {
	http.HandleFunc("/log", func(w http.ResponseWriter, r *http.Request) {
		msg, err := ioutil.ReadAll(r.Body)
		if err != nil || len(msg) == 0 {
			http.Error(w, "Bad request", http.StatusBadRequest)
			return
		}
		write(string(msg))
	}
}

func write(msg string) {
	log.Printf("%v\n", msg)")
}