import { resolve }  from 'path';
import react from '@vitejs/plugin-react';

module.exports = {
 plugins: [
  react({
    include: '**/*.disabled',
  }),
 ],
 root: resolve(__dirname, './src'),
 base: '/static/',
 server: {
   host: '127.0.0.1',
   port: 3000,
   open: false,
   watch: {
     usePolling: true,
     disableGlobbing: false,
   },
 },
 resolve: {
   extensions: ['.js', '.json'],
   alias: {
    '@': resolve(__dirname, './src')
  }
 },
 build: {
   outDir: resolve(__dirname, './dist'),
   assetsDir: 'static',
   manifest: true,
   emptyOutDir: true,
   target: 'es2015',
   rollupOptions: {
     input: {
       main: resolve(__dirname, './src/main.jsx'),
     },
   },
 },
};