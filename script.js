const graph = {
    nodes: [
        { id: 'A' }, { id: 'B' }, { id: 'C' }, { id: 'D' },
        { id: 'E' }, { id: 'F' }, { id: 'G' }, { id: 'H' }, { id: 'I' },
        { id: 'J' }, { id: 'K' }, { id: 'L' }, { id: 'M' }, { id: 'N' }
    ],
    edges: [
        { source: 'A', target: 'B', weight: 4 },
        { source: 'A', target: 'C', weight: 8 },
        { source: 'B', target: 'C', weight: 8 },
        { source: 'B', target: 'D', weight: 11 },
        { source: 'C', target: 'D', weight: 7 },
        { source: 'C', target: 'E', weight: 4 },
        { source: 'D', target: 'E', weight: 9 },
        { source: 'D', target: 'F', weight: 14 },
        { source: 'E', target: 'F', weight: 10 },
        { source: 'F', target: 'G', weight: 2 },
        { source: 'G', target: 'H', weight: 1 },
        { source: 'G', target: 'I', weight: 6 },
        { source: 'H', target: 'I', weight: 7 },
        { source: 'J', target: 'K', weight: 3 },
        { source: 'J', target: 'L', weight: 5 },
        { source: 'K', target: 'L', weight: 7 },
        { source: 'K', target: 'M', weight: 2 },
        { source: 'L', target: 'M', weight: 4 },
        { source: 'M', target: 'N', weight: 6 },
        { source: 'I', target: 'J', weight: 9 }
    ]
};
const width = document.getElementById("graph-container").clientWidth;
const height = document.getElementById("graph-container").clientHeight;

const svg = d3.select("#graph-container")
    .append("svg")
    .attr("width", width)
    .attr("height", height);

function getForces(width, height) {
    const isSmallScreen = width < 768;
    return {
        linkDistance: isSmallScreen ? 20 : 200,
        collideRadius: isSmallScreen ? 40 : 100,
        charge: isSmallScreen ? 20 : 500,
        centerForce: d3.forceCenter(width / 2, height / 2),
    };
}

const forces = getForces(width, height);

const simulation = d3.forceSimulation(graph.nodes)
    .force("link", d3.forceLink(graph.edges).id(d => d.id).distance(forces.linkDistance))
    .force("charge", d3.forceManyBody().strength(forces.charge))
    .force("collide", d3.forceCollide().radius(forces.collideRadius))
    .force("center", forces.centerForce);

const edges = svg.selectAll(".edge")
    .data(graph.edges)
    .enter()
    .append("line")
    .attr("class", "edge")
    .style("stroke", "black")
    .style("stroke-width", 2);

const edgeLabels = svg.selectAll(".edge-label")
    .data(graph.edges)
    .enter()
    .append("text")
    .attr("class", "edge-label")
    .text(d => d.weight)
    .style("font-size", "20px")
    .style("fill", "withe");

const nodes = svg.selectAll(".node")
    .data(graph.nodes)
    .enter()
    .append("circle")
    .attr("class", "node")
    .attr("r", 15)
    .style("fill", "lightblue")
    .style("stroke", "black")
    .style("stroke-width", 2);

const labels = svg.selectAll(".label")
    .data(graph.nodes)
    .enter()
    .append("text")
    .attr("class", "label")
    .text(d => d.id)
    .style("font-size", "16px")
    .style("text-anchor", "middle")
    .style("fill", "black");

simulation.on("tick", () => {
    edges.attr("x1", d => d.source.x)
        .attr("y1", d => d.source.y)
        .attr("x2", d => d.target.x)
        .attr("y2", d => d.target.y);

    nodes.attr("cx", d => d.x)
        .attr("cy", d => d.y);

    labels.attr("x", d => d.x)
        .attr("y", d => d.y + 5);

    edgeLabels.attr("x", d => (d.source.x + d.target.x) / 2)
        .attr("y", d => (d.source.y + d.target.y) / 2 + 5);
});

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}


let isRunning = false;

async function primStepByStep(startNodeId, speed) {
    edgeLabels.style("display", "block");
    bridges = []; // Limpiar aristas puente
    articulationPoints = new Set(); // Limpiar puntos de articulación
    isRunning = true;
    const visited = new Set([startNodeId]);
    const mstEdges = [];

    while (visited.size < graph.nodes.length && isRunning) {
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

            await sleep(speed);
        }
    }
    isRunning = false;
}

async function kruskalStepByStep(speed) {
    edgeLabels.style("display", "block");
    bridges = [];
    articulationPoints = new Set();
    isRunning = true;
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
        if (!isRunning) break;
        if (union(edge.source.id, edge.target.id)) {
            mstEdges.push(edge);

            edges.filter(d => d === edge)
                .style("stroke", "red")
                .style("stroke-width", 4);

            await sleep(speed);
        }
    }
    isRunning = false;
}

async function dijkstraStepByStep(startNodeId, speed) {
    bridges = [];
    articulationPoints = new Set();
    edgeLabels.style("display", "block");
    isRunning = true;
    const distanceLabels = svg.selectAll(".distance-label")
        .data(graph.nodes)
        .enter()
        .append("text")
        .attr("class", "distance-label")
        .text(d => "∞")
        .style("font-size", "20px")
        .style("fill", "orange")
        .attr("x", d => d.x)
        .attr("y", d => d.y - 15);

    const distances = {};
    const previous = {};
    const queue = new Set(graph.nodes.map(node => node.id));

    graph.nodes.forEach(node => {
        distances[node.id] = Infinity;
        previous[node.id] = null;
    });
    distances[startNodeId] = 0;

    distanceLabels.filter(d => d.id === startNodeId)
        .text("0");
    await sleep(speed);

    while (queue.size > 0 && isRunning) {
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

                distanceLabels.filter(d => d.id === neighbor)
                    .text(alt);

                edges.filter(d => d === edge)
                    .style("stroke", "red")
                    .style("stroke-width", 4);

                await sleep(speed);
            }
        }
    }
    isRunning = false;
}

async function bfsStepByStep(startNodeId, speed) {
    edgeLabels.style("display", "none");
    isRunning = true;
    const queue = [startNodeId];
    const visited = new Set([startNodeId]);
    const distances = {};


    graph.nodes.forEach(node => {
        distances[node.id] = Infinity;
    });
    distances[startNodeId] = 0;


    const distanceLabels = svg.selectAll(".distance-label")
        .data(graph.nodes)
        .enter()
        .append("text")
        .attr("class", "distance-label")
        .text(d => distances[d.id] === Infinity ? "∞" : distances[d.id])
        .style("font-size", "20px")
        .style("fill", "red")
        .attr("x", d => d.x)
        .attr("y", d => d.y - 15);

    while (queue.length > 0 && isRunning) {
        const current = queue.shift();


        nodes.filter(d => d.id === current)
            .style("fill", "green");


        const neighbors = graph.edges.filter(edge => edge.source.id === current || edge.target.id === current);
        for (const edge of neighbors) {
            const neighbor = edge.source.id === current ? edge.target.id : edge.source.id;
            if (!visited.has(neighbor)) {
                visited.add(neighbor);
                queue.push(neighbor);


                distances[neighbor] = distances[current] + 1;

                distanceLabels.filter(d => d.id === neighbor)
                    .text(distances[neighbor]);

                edges.filter(d => d === edge)
                    .style("stroke", "red")
                    .style("stroke-width", 4);

                await sleep(speed);
            }
        }
    }
    isRunning = false;
}

let bridges = [];
let articulationPoints = new Set();

async function dfsStepByStep(startNodeId, speed) {

    edgeLabels.style("display", "none");
    isRunning = true;
    const disc = {};
    const low = {};
    const parent = {};
    let time = 0;


    graph.nodes.forEach(node => {
        disc[node.id] = -1;
        low[node.id] = -1;
        parent[node.id] = null;
    });


    async function dfs(u) {
        if (!isRunning) return;


        disc[u] = low[u] = ++time;


        let children = 0;


        const neighbors = graph.edges.filter(edge => edge.source.id === u || edge.target.id === u);
        for (const edge of neighbors) {
            const v = edge.source.id === u ? edge.target.id : edge.source.id;

            if (disc[v] === -1) {
                children++;
                parent[v] = u;


                edges.filter(d => d === edge)
                    .style("stroke", "cyan")
                    .style("stroke-width", 4);

                nodes.filter(d => d.id === v)
                    .style("fill", "yellow");

                await sleep(speed);

                await dfs(v);


                low[u] = Math.min(low[u], low[v]);


                if (parent[u] === null && children > 1) {
                    articulationPoints.add(u);
                }
                if (parent[u] !== null && low[v] >= disc[u]) {
                    articulationPoints.add(u);
                }


                if (low[v] > disc[u]) {
                    bridges.push(edge);
                }
            } else if (v !== parent[u]) {
                low[u] = Math.min(low[u], disc[v]);
            }
        }
    }


    await dfs(startNodeId);


    edges.filter(d => bridges.includes(d))
        .attr("class", "edge bridge");
    nodes.filter(d => bridges.includes(d))
        .style("fill", "red");

    nodes.filter(d => articulationPoints.has(d.id))
        .attr("class", "node articulation-point");


    const bridgeInfo = bridges.length > 0
        ? `🔗 <strong>Aristas puente:</strong> ${bridges.map(e => `${e.source.id}-${e.target.id}`).join(", ")}`
        : "🔗 No hay aristas puente.";

    const articulationInfo = articulationPoints.size > 0
        ? `📍 <strong>Puntos de articulación:</strong> ${Array.from(articulationPoints).join(", ")}`
        : "📍 No hay puntos de articulación.";

    algorithmInfo.innerHTML = `${bridgeInfo}<br>${articulationInfo}`;

    isRunning = false;
}

function resetGraph() {
    isRunning = false;
    edges.style("stroke", "#999")
        .style("stroke-width", 2)
        .attr("class", "edge");
    nodes.style("fill", "lightblue")
        .attr("class", "node");
    svg.selectAll(".distance-label").remove();
    simulation.stop();
    bridges = [];
    articulationPoints = new Set();
}

document.getElementById("start-button").addEventListener("click", () => {
    const algorithm = document.getElementById("algorithm-select").value;
    const startNodeId = document.getElementById("start-node-select").value;
    const speed = parseInt(document.getElementById("speed-slider").value);
    resetGraph();
    if (algorithm === "prim") {
        primStepByStep(startNodeId, speed);
    } else if (algorithm === "kruskal") {
        kruskalStepByStep(speed);
    } else if (algorithm === "dijkstra") {
        dijkstraStepByStep(startNodeId, speed);
    } else if (algorithm === "bfs") {
        bfsStepByStep(startNodeId, speed);
    } else if (algorithm === "dfs") {
        dfsStepByStep(startNodeId, speed);
    }
});

document.getElementById("reset-button").addEventListener("click", () => {
    resetGraph();
});

window.addEventListener("resize", () => {
    const newWidth = window.innerWidth;
    const newHeight = window.innerHeight;
    svg.attr("width", newWidth)
        .attr("height", newHeight);
    simulation.force("center", d3.forceCenter(newWidth / 2, newHeight / 2))
        .alpha(0.3).restart();
});

const startNodeSelect = document.getElementById("start-node-select");

graph.nodes.forEach(node => {
    const option = document.createElement("option");
    option.value = node.id;
    option.text = node.id;
    startNodeSelect.appendChild(option);
});

const algorithmInfo = document.getElementById("algorithm-info");
algorithmInfo.textContent = "Prim's Algorithm: Finds the minimum spanning tree for a weighted undirected graph.";
document.getElementById("algorithm-select").addEventListener("change", () => {
    const algorithm = document.getElementById("algorithm-select").value;
    let info = "";
    if (algorithm === "prim") {
        info = "Prim's Algorithm: Finds the minimum spanning tree for a weighted undirected graph.";
    } else if (algorithm === "kruskal") {
        info = "Kruskal's Algorithm: Finds the minimum spanning tree for a weighted undirected graph.";
    } else if (algorithm === "dijkstra") {
        info = "Dijkstra's Algorithm: Finds the shortest path from a start node to all other nodes in a weighted graph.";
    } else if (algorithm === "bfs") {
        info = "Breadth-First Search (BFS): Explores all nodes level by level from a start node.";
    } else if (algorithm === "dfs") {
        info = "Depth-First Search (DFS): Explores as far as possible along each branch before backtracking.";
    }
    algorithmInfo.textContent = info;
});