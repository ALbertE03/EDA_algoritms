
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

// Configuración del SVG
const width = 800, height = 500;
const svg = d3.select("#graph-container")
    .append("svg")
    .attr("width", width)
    .attr("height", height);

// Escalador para posicionar los nodos
const simulation = d3.forceSimulation(graph.nodes)
    .force("link", d3.forceLink(graph.edges).id(d => d.id).distance(200)) // Aumentar distancia
    .force("charge", d3.forceManyBody().strength(-1000)) // Aumentar repulsión
    .force("collide", d3.forceCollide().radius(40))
    .force("center", d3.forceCenter(width / 2, height / 2));

// Dibujar las aristas
const edges = svg.selectAll(".edge")
    .data(graph.edges)
    .enter()
    .append("line")
    .attr("class", "edge")
    .style("stroke", "#999")
    .style("stroke-width", 2);

// Etiquetas de peso de las aristas
const edgeLabels = svg.selectAll(".edge-label")
    .data(graph.edges)
    .enter()
    .append("text")
    .attr("class", "edge-label")
    .text(d => d.weight)
    .style("font-size", "12px")
    .style("fill", "#333");

// Dibujar los nodos
const nodes = svg.selectAll(".node")
    .data(graph.nodes)
    .enter()
    .append("circle")
    .attr("class", "node")
    .attr("r", 10)
    .style("fill", "lightblue");

// Etiquetas de los nodos
const labels = svg.selectAll(".label")
    .data(graph.nodes)
    .enter()
    .append("text")
    .attr("class", "label")
    .text(d => d.id)
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
        .attr("y", d => d.y + 20);

    // Posicionar las etiquetas de peso en el centro de las aristas
    edgeLabels.attr("x", d => (d.source.x + d.target.x) / 2)
        .attr("y", d => (d.source.y + d.target.y) / 2);
});

// Función para pausar la ejecución
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// Algoritmo de Prim paso a paso
async function primStepByStep(startNodeId) {
    const visited = new Set([startNodeId]); // Nodos visitados
    const mstEdges = []; // Aristas del MST

    while (visited.size < graph.nodes.length) {
        let minEdge = null;
        let minWeight = Infinity;

        // Encontrar la arista de menor peso que conecta un nodo visitado con uno no visitado
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

            // Resaltar la arista seleccionada
            edges.filter(d => d === minEdge)
                .style("stroke", "red")
                .style("stroke-width", 4);

            // Pausa para visualizar el paso
            await sleep(1000);
        }
    }
}

// Función para reiniciar el gráfico
function resetGraph() {
    edges.style("stroke", "#999")
        .style("stroke-width", 2);
    nodes.style("fill", "lightblue");
}

// Iniciar el algoritmo seleccionado
document.getElementById("start-button").addEventListener("click", () => {
    const algorithm = document.getElementById("algorithm-select").value;
    resetGraph();
    if (algorithm === "prim") {
        primStepByStep('A');
    }
    // Aquí puedes agregar más algoritmos
});

// Reiniciar el gráfico
document.getElementById("reset-button").addEventListener("click", resetGraph);