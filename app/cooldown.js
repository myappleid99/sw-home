const cyberData = [
            {
               id: 1,
               timestamp: 1620312595377
            }
         ];
         var db;
         var request = window.indexedDB.open("Cyber", 1);


         request.onsuccess = function(event) {
            db = request.result;
         };

         request.onupgradeneeded = function(event) {
            var db = event.target.result;
            var objectStore = db.createObjectStore("cyber", {keyPath: "id"});

            for (var i in cyberData) {
               objectStore.add(cyberData[i]);
            }
         }
