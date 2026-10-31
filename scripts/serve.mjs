import http from 'node:http';
import {readFile,stat} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
const root=fileURLToPath(new URL('../dist/',import.meta.url));
const mime={'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.js':'text/javascript; charset=utf-8','.json':'application/json; charset=utf-8','.svg':'image/svg+xml','.ttf':'font/ttf','.txt':'text/plain; charset=utf-8','.webmanifest':'application/manifest+json'};
http.createServer(async(req,res)=>{try{const rel=decodeURIComponent(new URL(req.url,'http://localhost').pathname),target=path.resolve(root,'.'+rel);if(!target.startsWith(root)){res.writeHead(403);res.end();return}const file=(await stat(target)).isDirectory()?path.join(target,'index.html'):target;res.setHeader('Content-Type',mime[path.extname(file)]||'application/octet-stream');res.setHeader('Cache-Control','no-cache');res.end(await readFile(file))}catch{res.writeHead(404);res.end('Not found')}}).listen(3000,'127.0.0.1',()=>console.log('Al-Hayat: http://localhost:3000 — Ctrl+C to stop.'));
