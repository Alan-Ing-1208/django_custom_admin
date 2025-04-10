<script>
    const ctx = document.getElementById('myChart').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
            datasets: [{
                label: 'Revenue',
                data: [12, 19, 3, 5, 15],
                backgroundColor: 'rgba(0, 255, 255, 0.2)',
                borderColor: '#00ffff',
                borderWidth: 2,
                tension: 0.4,
                fill: true
            }]
        },
        options: {
            plugins: {
                legend: {
                    labels: {
                        color: '#fff'
                    }
                }
            },
            scales: {
                x: {
                    ticks: { color: '#fff' },
                    grid: { color: '#444' }
                },
                y: {
                    ticks: { color: '#fff' },
                    grid: { color: '#444' }
                }
            }
        }
    });
</script>

<script>
    const ctx2 = document.getElementById('usersChart').getContext('2d');
    const usersChart = new Chart(ctx2, {
        type: 'bar',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
            datasets: [{
                label: 'Users',
                data: [200, 300, 400, 350, 500],
                backgroundColor: 'rgba(255, 99, 132, 0.5)',
                borderColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 1
            }]
        },
        options: {
            plugins: {
                legend: {
                    labels: {
                        color: '#fff'
                    }
                }
            },
            scales: {
                x: {
                    ticks: { color: '#fff' },
                    grid: { color: '#444' }
                },
                y: {
                    ticks: { color: '#fff' },
                    grid: { color: '#444' }
                }
            }
        }
    });
</script>
