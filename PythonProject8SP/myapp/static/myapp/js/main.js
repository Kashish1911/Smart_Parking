function startPolling(url, cb, interval) {
  // initial fetch
  fetch(url).then(r=>r.json()).then(data=>cb(data)).catch(()=>{});
  if (!interval) return;
  setInterval(()=> {
    fetch(url).then(r=>r.json()).then(data=>cb(data)).catch(()=>{});
  }, interval);
}
