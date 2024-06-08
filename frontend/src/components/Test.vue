<script setup>
import { ref, onMounted } from 'vue'


const data = ref('')

const fetchData = async () => {
    try {
        const response = await fetch('http://127.0.0.1:5000/api/test', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },

        })
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`)
        }

        return await response.json()

    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

onMounted(async () => {
    data.value = await fetchData()
})
</script>

<template>

  <div >
    <p> <b>Succesfully fetched data:</b> {{ data }}</p>
    <p>
      Edit
      <code>../app/resources/</code> update <b>a,b</b> and reload to test 
    </p>
  </div>

</template>

<style scoped>

</style>
