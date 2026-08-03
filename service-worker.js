const CACHE_NAME = "beyond-ball-v3";

const FILES = [
    "index.html",
    "dashboard.html",
    "archive.html",
    "manifest.json"
];

// Install
self.addEventListener("install", event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => cache.addAll(FILES))
    );
});

// Activate
self.addEventListener("activate", event => {
    event.waitUntil(
        caches.keys().then(keys =>
            Promise.all(
                keys.map(key => {
                    if (key !== CACHE_NAME) {
                        return caches.delete(key);
                    }
                })
            )
        )
    );
});

// Fetch
self.addEventListener("fetch", event => {

    // Never cache news.json
    if (event.request.url.includes("news.json")) {

        event.respondWith(
            fetch(event.request)
                .catch(() => caches.match(event.request))
        );

        return;
    }

    event.respondWith(
        caches.match(event.request).then(response => {
            return response || fetch(event.request);
        })
    );
});
