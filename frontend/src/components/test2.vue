<script setup>
import { ref, onMounted } from 'vue'

const data = ref([])

const fetch_data= async () => {
    try {

        const response = await fetch('http://127.0.0.1/5000/api/test2', {
            method: 'GET',
            headers: {
            'content-type': 'application/json',
            },
    })

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`)
        }

        return await response.json()

    }
    catch (error) {
        console.error('Error fetching data:', error);
    }}
onMounted(async () => {
    data.value = await fetch_data()
})
</script>

<template>
<table>
    <th>
        <td> First Word</td>
    
    </th>
<tr>
    <td> {{ data }}</td>
</tr>
</table>
</template>
<style>
</style>
