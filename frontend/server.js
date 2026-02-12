import { createServer } from 'vite'
import vue from '@vitejs/plugin-vue'

(async () => {
    try {
        const server = await createServer({
            // Explicitly disable config file loading to avoid EPERM errors
            configFile: false,
            root: process.cwd(),
            plugins: [vue()],
            server: {
                port: 5173
            }
        })
        await server.listen()

        server.printUrls()
    } catch (e) {
        console.error('Error starting server:', e)
    }
})()
