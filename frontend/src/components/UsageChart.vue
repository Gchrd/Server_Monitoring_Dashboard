<template>
  <div class="chart-container">
    <h3>{{ title }}</h3>
    <Line :data="chartData" :options="chartOptions" />
  </div>
</template>

<script>
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js'
import { Line } from 'vue-chartjs'

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
)

export default {
  name: 'UsageChart',
  components: { Line },
  props: {
    title: String,
    labels: Array,
    data: Array,
    color: {
      type: String,
      default: '#3b82f6'
    }
  },
  computed: {
    chartData() {
      return {
        labels: this.labels,
        datasets: [
          {
            label: this.title,
            backgroundColor: this.color,
            borderColor: this.color,
            data: this.data,
            tension: 0.4,
            fill: false
          }
        ]
      }
    },
    chartOptions() {
      return {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            display: false
          }
        },
        scales: {
            y: {
                beginAtZero: true,
                max: 100
            }
        }
      }
    }
  }
}
</script>

<style scoped>
.chart-container {
  background: white;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  height: 300px;
  position: relative;
}
h3 {
    margin-top: 0;
    margin-bottom: 1rem;
    color: #4b5563;
    font-size: 1rem;
    font-weight: 600;
}
</style>
