const graph = {
    nodes: [
        { id: 'A' }, { id: 'B' }, { id: 'C' }, { id: 'D' },
        { id: 'E' }, { id: 'F' }, { id: 'G' }, { id: 'H' }, { id: 'I' }
    ],
    edges: [
        { source: 'A', target: 'B', weight: 4 },
        { source: 'A', target: 'H', weight: 8 },
        { source: 'B', target: 'C', weight: 8 },
        { source: 'B', target: 'H', weight: 11 },
        { source: 'C', target: 'D', weight: 7 },
        { source: 'C', target: 'F', weight: 4 },
        { source: 'C', target: 'I', weight: 2 },
        { source: 'D', target: 'E', weight: 9 },
        { source: 'D', target: 'F', weight: 14 },
        { source: 'E', target: 'F', weight: 10 },
        { source: 'F', target: 'G', weight: 2 },
        { source: 'G', target: 'H', weight: 1 },
        { source: 'G', target: 'I', weight: 6 },
        { source: 'H', target: 'I', weight: 7 }
    ]
};

const width = document.getElementById("graph-container").clientWidth;
const height = document.getElementById("graph-container").clientHeight;

const svg = d3.select("#graph-container")
    .append("svg")
    .attr("width", width)
    .attr("height", height);

function getForces(width, height) {
    const isSmallScreen = width < 768; // para pantallas pequeñas
    return {
        linkDistance: isSmallScreen ? 0 : 200,
        collideRadius: isSmallScreen ? 0 : 40,
        charge: isSmallScreen ? -500 : -1000,
        centerForce: d3.forceCenter(width / 2, height / 2),
    };
}


const forces = getForces(width, height);


const simulation = d3.forceSimulation(graph.nodes)
    .force("link", d3.forceLink(graph.edges).id(d => d.id).distance(forces.linkDistance))
    .force("charge", d3.forceManyBody().strength(forces.charge))
    .force("collide", d3.forceCollide().radius(forces.collideRadius))
    .force("center", forces.centerForce)

// Dibujar las aristas
const edges = svg.selectAll(".edge")
    .data(graph.edges)
    .enter()
    .append("line")
    .attr("class", "edge")
    .style("stroke", "#999")
    .style("stroke-width", 2);

// Etiquetas de peso de las aristas (más grandes)
const edgeLabels = svg.selectAll(".edge-label")
    .data(graph.edges)
    .enter()
    .append("text")
    .attr("class", "edge-label")
    .text(d => d.weight)
    .style("font-size", "14px") // Tamaño de fuente más grande
    .style("fill", "#333");

// Dibujar los nodos
const nodes = svg.selectAll(".node")
    .data(graph.nodes)
    .enter()
    .append("circle")
    .attr("class", "node")
    .attr("r", 15) // Radio más grande
    .style("fill", "lightblue")
    .style("stroke", "#333")
    .style("stroke-width", 2);


const labels = svg.selectAll(".label")
    .data(graph.nodes)
    .enter()
    .append("text")
    .attr("class", "label")
    .text(d => d.id)
    .style("font-size", "16px") // Tamaño de fuente más grande
    .style("text-anchor", "middle")
    .style("fill", "black");



// Actualizar la posición de los elementos en cada tick del simulador
simulation.on("tick", () => {
    edges.attr("x1", d => d.source.x)
        .attr("y1", d => d.source.y)
        .attr("x2", d => d.target.x)
        .attr("y2", d => d.target.y);

    nodes.attr("cx", d => d.x)
        .attr("cy", d => d.y);

    labels.attr("x", d => d.x)
        .attr("y", d => d.y + 5); // Ajustar posición de las etiquetas de los nodos

    edgeLabels.attr("x", d => (d.source.x + d.target.x) / 2)
        .attr("y", d => (d.source.y + d.target.y) / 2 + 5); // Ajustar posición de los pesos de las aristas

    distanceLabels.attr("x", d => d.x)
        .attr("y", d => d.y - 20); // Ajustar posición de las etiquetas de distancia
});


// Función para pausar la ejecución
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// Algoritmo de Prim paso a paso
async function primStepByStep(startNodeId) {
    const visited = new Set([startNodeId]);
    const mstEdges = [];

    while (visited.size < graph.nodes.length) {
        let minEdge = null;
        let minWeight = Infinity;

        graph.edges.forEach(edge => {
            if (
                (visited.has(edge.source.id) && !visited.has(edge.target.id)) ||
                (visited.has(edge.target.id) && !visited.has(edge.source.id))
            ) {
                if (edge.weight < minWeight) {
                    minWeight = edge.weight;
                    minEdge = edge;
                }
            }
        });

        if (minEdge) {
            mstEdges.push(minEdge);
            visited.add(minEdge.source.id);
            visited.add(minEdge.target.id);

            edges.filter(d => d === minEdge)
                .style("stroke", "red")
                .style("stroke-width", 4);

            nodes.filter(d => d.id === minEdge.source.id || d.id === minEdge.target.id)
                .style("fill", "orange");

            await sleep(1000);
        }
    }
}

// Algoritmo de Kruskal paso a paso
async function kruskalStepByStep() {

    const sortedEdges = graph.edges.slice().sort((a, b) => a.weight - b.weight);
    const parent = {};
    const mstEdges = [];

    graph.nodes.forEach(node => parent[node.id] = node.id);

    function find(u) {
        if (parent[u] !== u) parent[u] = find(parent[u]);
        return parent[u];
    }

    function union(u, v) {
        const rootU = find(u);
        const rootV = find(v);
        if (rootU !== rootV) {
            parent[rootV] = rootU;
            return true;
        }
        return false;
    }

    for (const edge of sortedEdges) {
        if (union(edge.source.id, edge.target.id)) {
            mstEdges.push(edge);

            edges.filter(d => d === edge)
                .style("stroke", "red")
                .style("stroke-width", 4);

            await sleep(1000);
        }
    }
}


// Algoritmo de Dijkstra paso a paso con actualización de etiquetas
async function dijkstraStepByStep(startNodeId) {

    const distanceLabels = svg.selectAll(".distance-label")
        .data(graph.nodes)
        .enter()
        .append("text")
        .attr("class", "distance-label")
        .text(d => "∞")
        .style("font-size", "20px")
        .style("fill", "red")
        .attr("x", d => d.x)
        .attr("y", d => d.y - 15)
    const distances = {};
    const previous = {};
    const queue = new Set(graph.nodes.map(node => node.id));

    graph.nodes.forEach(node => {
        distances[node.id] = Infinity;
        previous[node.id] = null;
    });
    distances[startNodeId] = 0;

    // Actualizar la etiqueta del nodo de inicio
    distanceLabels.filter(d => d.id === startNodeId)
        .text("0");
    await sleep(1000);
    while (queue.size > 0) {
        let minNode = null;
        for (const node of queue) {
            if (minNode === null || distances[node] < distances[minNode]) {
                minNode = node;
            }
        }

        queue.delete(minNode);

        if (distances[minNode] === Infinity) break;

        const neighbors = graph.edges.filter(edge => edge.source.id === minNode || edge.target.id === minNode);
        for (const edge of neighbors) {
            const neighbor = edge.source.id === minNode ? edge.target.id : edge.source.id;
            const alt = distances[minNode] + edge.weight;
            if (alt < distances[neighbor]) {
                distances[neighbor] = alt;
                previous[neighbor] = minNode;

                // Actualizar la etiqueta del nodo vecino
                distanceLabels.filter(d => d.id === neighbor)
                    .text(alt);

                edges.filter(d => d === edge)
                    .style("stroke", "blue")
                    .style("stroke-width", 4);

                await sleep(1000);
            }
        }
    }
}
// Algoritmo de BFS paso a paso
async function bfsStepByStep(startNodeId) {
    const queue = [startNodeId];
    const visited = new Set([startNodeId]);

    while (queue.length > 0) {
        const current = queue.shift();

        nodes.filter(d => d.id === current)
            .style("fill", "green");

        const neighbors = graph.edges.filter(edge => edge.source.id === current || edge.target.id === current);
        for (const edge of neighbors) {
            const neighbor = edge.source.id === current ? edge.target.id : edge.source.id;
            if (!visited.has(neighbor)) {
                visited.add(neighbor);
                queue.push(neighbor);

                edges.filter(d => d === edge)
                    .style("stroke", "purple")
                    .style("stroke-width", 4);

                await sleep(1000);
            }
        }
    }
}

// Algoritmo de DFS paso a paso
async function dfsStepByStep(startNodeId) {
    const stack = [startNodeId];
    const visited = new Set([startNodeId]);

    while (stack.length > 0) {
        const current = stack.pop();

        nodes.filter(d => d.id === current)
            .style("fill", "yellow");

        const neighbors = graph.edges.filter(edge => edge.source.id === current || edge.target.id === current);
        for (const edge of neighbors) {
            const neighbor = edge.source.id === current ? edge.target.id : edge.source.id;
            if (!visited.has(neighbor)) {
                visited.add(neighbor);
                stack.push(neighbor);

                edges.filter(d => d === edge)
                    .style("stroke", "cyan")
                    .style("stroke-width", 4);

                await sleep(1000);
            }
        }
    }
}

// Función para reiniciar el gráfico
function resetGraph() {
    edges.style("stroke", "#999")
        .style("stroke-width", 2);
    nodes.style("fill", "lightblue");
    svg.selectAll(".distance-label").remove();
}

// Iniciar el algoritmo seleccionado
document.getElementById("start-button").addEventListener("click", () => {
    const algorithm = document.getElementById("algorithm-select").value;
    resetGraph();
    if (algorithm === "prim") {
        primStepByStep('A');
    } else if (algorithm === "kruskal") {
        kruskalStepByStep();
    } else if (algorithm === "dijkstra") {
        dijkstraStepByStep('A');
    } else if (algorithm === "bfs") {
        bfsStepByStep('A');
    } else if (algorithm === "dfs") {
        dfsStepByStep('A');
    }
});

// Reiniciar el gráfico
document.getElementById("reset-button").addEventListener("click", resetGraph);

// Hacer el gráfico responsive
window.addEventListener("resize", () => {
    const newWidth = window.innerWidth * 0.9;
    const newHeight = window.innerHeight * 0.7;
    svg.attr("width", newWidth)
        .attr("height", newHeight);
    simulation.force("center", d3.forceCenter(newWidth / 2, newHeight / 2))
        .alpha(0.3).restart();
});