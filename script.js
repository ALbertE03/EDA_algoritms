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

        { source: 'G', target: 'I', weight: 6 },

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
        linkDistance: isSmallScreen ? 20 : 100,
        collideRadius: isSmallScreen ? 40 : 100,
        charge: isSmallScreen ? 20 : 300,
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
    .style("font-size", "16px")
    .style("font-weight", "bold")
    .style("fill", "#ffffff")
    .style("text-shadow", "0 0 3px #000000, 0 0 2px #000000, 0 0 1px #000000");

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

    // Conjunto para nodos visitados globalmente
    const globalVisited = new Set();
    const mstEdges = [];

    // Seguir ejecutando Prim para cada componente no visitado
    while (globalVisited.size < graph.nodes.length && isRunning) {
        // Si tenemos un nodo de inicio específico, usarlo para el primer componente
        // Para los componentes restantes, tomar cualquier nodo no visitado
        let currentStart;
        if (globalVisited.size === 0) {
            currentStart = startNodeId;
        } else {
            // Encontrar el primer nodo no visitado para el siguiente componente
            currentStart = graph.nodes.find(node => !globalVisited.has(node.id))?.id;
            if (!currentStart) break; // No hay más nodos para visitar

            // Mostrar mensaje de nuevo componente
            algorithmInfo.innerHTML += `<p style="color: #f97316;">Iniciando nuevo componente desde el nodo ${currentStart}</p>`;
            await sleep(speed);
        }

        // Visitar el nodo inicial del componente actual
        globalVisited.add(currentStart);
        const componentVisited = new Set([currentStart]);

        // Resaltar nodo inicial de cada componente
        nodes.filter(d => d.id === currentStart)
            .transition().duration(200)
            .style("fill", "#c084fc") // Púrpura para nodo inicial de componente
            .style("stroke", "#7e22ce")
            .style("stroke-width", 3);

        await sleep(speed);

        // Ejecutar Prim para el componente actual
        let componentComplete = false;
        while (!componentComplete && isRunning) {
            let minEdge = null;
            let minWeight = Infinity;

            // Buscar la arista de menor peso que conecta un nodo visitado con uno no visitado
            graph.edges.forEach(edge => {
                if (
                    (componentVisited.has(edge.source.id) && !componentVisited.has(edge.target.id)) ||
                    (componentVisited.has(edge.target.id) && !componentVisited.has(edge.source.id))
                ) {
                    if (edge.weight < minWeight) {
                        minWeight = edge.weight;
                        minEdge = edge;
                    }
                }
            });

            if (minEdge) {
                // Agregar la arista al MST
                mstEdges.push(minEdge);

                // Actualizar conjuntos de nodos visitados
                const newNode = componentVisited.has(minEdge.source.id) ? minEdge.target.id : minEdge.source.id;
                componentVisited.add(newNode);
                globalVisited.add(newNode);

                // Visualizar la arista y nodos
                edges.filter(d => d === minEdge)
                    .transition().duration(200)
                    .style("stroke", "#10b981") // Verde para MST
                    .style("stroke-width", 4)
                    .style("opacity", 1);

                nodes.filter(d => d.id === newNode)
                    .transition().duration(200)
                    .style("fill", "#f97316") // Naranja para nodos visitados
                    .style("stroke", "#ea580c")
                    .style("stroke-width", 2);

                await sleep(speed);
            } else {
                // No se encontraron más aristas para el componente actual
                componentComplete = true;
            }
        }
    }

    // Verificar si todos los nodos fueron visitados
    if (globalVisited.size < graph.nodes.length) {
        algorithmInfo.innerHTML += `<p style="color: #ef4444;"><strong>Nota:</strong> El grafo no es completamente conexo. Se han encontrado ${mstEdges.length} aristas para un bosque de expansión mínima.</p>`;
    } else {
        algorithmInfo.innerHTML += `<p style="color: #10b981;"><strong>Éxito:</strong> Árbol de expansión mínima encontrado con ${mstEdges.length} aristas.</p>`;
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
    const componentCount = {}; // Para contar nodos por componente

    // Inicializar cada nodo en su propio conjunto
    graph.nodes.forEach(node => {
        parent[node.id] = node.id;
        componentCount[node.id] = 1; // Iniciar con un nodo por componente
    });

    function find(u) {
        if (parent[u] !== u) parent[u] = find(parent[u]);
        return parent[u];
    }

    function union(u, v) {
        const rootU = find(u);
        const rootV = find(v);
        if (rootU !== rootV) {
            // El conjunto más pequeño se une al más grande (optimización)
            if (componentCount[rootU] < componentCount[rootV]) {
                parent[rootU] = rootV;
                componentCount[rootV] += componentCount[rootU];
            } else {
                parent[rootV] = rootU;
                componentCount[rootU] += componentCount[rootV];
            }
            return true;
        }
        return false;
    }

    // Color para diferentes componentes
    const getComponentColor = (componentId) => {
        const hue = (componentId.charCodeAt(0) * 20) % 360;
        return `hsl(${hue}, 80%, 60%)`;
    };

    // Inicialmente colorear cada nodo como su propio componente
    for (const node of graph.nodes) {
        nodes.filter(d => d.id === node.id)
            .transition().duration(300)
            .style("fill", getComponentColor(node.id));

        await sleep(speed / 4);
    }

    algorithmInfo.innerHTML = "<p>Ordenando aristas por peso...</p>";
    await sleep(speed);

    algorithmInfo.innerHTML += "<p>Construyendo bosque de expansión mínima...</p>";

    let componentCount2 = graph.nodes.length; // Iniciar con N componentes

    for (const edge of sortedEdges) {
        if (!isRunning) break;

        // Resaltar la arista actual que estamos considerando
        edges.filter(d => d === edge)
            .transition().duration(200)
            .style("stroke", "#f97316") // Naranja para arista considerada
            .style("stroke-width", 4)
            .style("opacity", 1);

        nodes.filter(d => d.id === edge.source.id || d.id === edge.target.id)
            .transition().duration(200)
            .style("stroke", "#000000")
            .style("stroke-width", 3);

        algorithmInfo.innerHTML += `<p>Evaluando arista ${edge.source.id}-${edge.target.id} con peso ${edge.weight}...</p>`;

        await sleep(speed);

        // Verificar si agregar esta arista no creará un ciclo
        if (union(edge.source.id, edge.target.id)) {
            mstEdges.push(edge);
            componentCount2--; // Reducir el número de componentes

            // Actualizar la visualización para mostrar que la arista es parte del MST
            edges.filter(d => d === edge)
                .transition().duration(200)
                .style("stroke", "#10b981") // Verde para el MST
                .style("stroke-width", 4)
                .style("opacity", 1);

            algorithmInfo.innerHTML += `<p style="color: #10b981;">✅ Arista ${edge.source.id}-${edge.target.id} añadida al MST</p>`;

            // Actualizar color de todos los nodos en el mismo componente
            const rootComponent = find(edge.source.id);
            const componentColor = getComponentColor(rootComponent);

            for (const node of graph.nodes) {
                if (find(node.id) === rootComponent) {
                    nodes.filter(d => d.id === node.id)
                        .transition().duration(300)
                        .style("fill", componentColor);
                }
            }
        } else {
            // La arista crearía un ciclo, resaltarlo brevemente y luego resetear
            edges.filter(d => d === edge)
                .transition().duration(200)
                .style("stroke", "#ef4444") // Rojo para aristas rechazadas
                .style("stroke-width", 2)
                .style("opacity", 0.5);

            algorithmInfo.innerHTML += `<p style="color: #ef4444;">❌ Arista ${edge.source.id}-${edge.target.id} rechazada (crearía ciclo)</p>`;
        }

        await sleep(speed / 2);
    }

    // Verificar si se formó un solo árbol o un bosque
    if (componentCount2 > 1) {
        algorithmInfo.innerHTML += `<p style="color: #f97316;"><strong>Nota:</strong> El grafo no es conexo. Se ha formado un bosque de expansión mínima con ${componentCount2} componentes.</p>`;
    } else {
        algorithmInfo.innerHTML += `<p style="color: #10b981;"><strong>Éxito:</strong> Árbol de expansión mínima completo encontrado con ${mstEdges.length} aristas.</p>`;
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
async function bellmanFordStepByStep(startNodeId, speed) {
    edgeLabels.style("display", "block");
    isRunning = true;
    const distances = {};
    const previous = {};
    graph.nodes.forEach(node => {
        distances[node.id] = Infinity;
        previous[node.id] = null;
    });
    distances[startNodeId] = 0;


    const distanceLabels = svg.selectAll(".distance-label")
        .data(graph.nodes)
        .enter()
        .append("text")
        .attr("class", "distance-label")
        .text(d => distances[d.id] === Infinity ? "∞" : distances[d.id])
        .style("font-size", "20px")
        .style("fill", "orange")
        .attr("x", d => d.x)
        .attr("y", d => d.y - 15);

    //relajar
    for (let i = 0; i < graph.nodes.length - 1 && isRunning; i++) {
        for (const edge of graph.edges) {
            if (!isRunning) break;


            const u = edge.source.id;
            const v = edge.target.id;
            const weight = edge.weight;


            if (distances[u] !== Infinity && distances[u] + weight < distances[v]) {
                distances[v] = distances[u] + weight;
                previous[v] = u;


                distanceLabels.filter(d => d.id === v)
                    .text(distances[v]);


                edges.filter(d => d === edge)
                    .style("stroke", "red")
                    .style("stroke-width", 4);

                nodes.filter(d => d.id === v)
                    .style("fill", "orange");

                await sleep(speed);
            }

            // Relajar de v a u
            if (distances[v] !== Infinity && distances[v] + weight < distances[u]) {
                distances[u] = distances[v] + weight;
                previous[u] = v;


                distanceLabels.filter(d => d.id === u)
                    .text(distances[u]);


                edges.filter(d => d === edge)
                    .style("stroke", "red")
                    .style("stroke-width", 4);

                nodes.filter(d => d.id === u)
                    .style("fill", "orange");

                await sleep(speed);
            }
        }
    }

    // Verificar ciclos negativos
    for (const edge of graph.edges) {
        const u = edge.source.id;
        const v = edge.target.id;
        const weight = edge.weight;

        if (distances[u] !== Infinity && distances[u] + weight < distances[v]) {
            algorithmInfo.innerHTML = "⚠️ <strong>Ciclo negativo detectado!</strong>";
            isRunning = false;
            return;
        }
        if (distances[v] !== Infinity && distances[v] + weight < distances[u]) {
            algorithmInfo.innerHTML = "⚠️ <strong>Ciclo negativo detectado!</strong>";
            isRunning = false;
            return;
        }
    }

    algorithmInfo.innerHTML = "✅ <strong>Bellman-Ford completado!</strong>";
    isRunning = false;
}
async function detectAndHighlightCycles(speed, startN) {
    edgeLabels.style("display", "none");
    isRunning = true;

    const cycles = new Set();
    const normalizedCycles = new Set();

    async function dfs(nodeId, path, parentId) {
        if (!isRunning) return;

        if (path.includes(nodeId)) {
            const cycle = path.slice(path.indexOf(nodeId)).concat(nodeId);
            const normalizedCycle = normalizeCycle(cycle);

            if (!normalizedCycles.has(normalizedCycle)) {
                normalizedCycles.add(normalizedCycle);
                cycles.add(cycle.join("-"));


                await highlightCycle(cycle, speed);


                await resetCycle(cycle);
            }
            return;
        }

        nodes.filter(d => d.id === nodeId)
            .style("fill", "yellow");

        await sleep(speed);


        const neighbors = graph.edges
            .filter(edge => edge.source.id === nodeId || edge.target.id === nodeId)
            .map(edge => edge.source.id === nodeId ? edge.target.id : edge.source.id);


        for (const neighbor of neighbors) {
            if (neighbor !== parentId) {
                await dfs(neighbor, [...path, nodeId], nodeId);
            }
        }


        nodes.filter(d => d.id === nodeId)
            .style("fill", "lightblue");
    }

    function normalizeCycle(cycle) {
        const sortedCycle = [...cycle].sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0));
        return sortedCycle.join("-");
    }

    async function highlightCycle(cycle, speed) {

        for (let i = 0; i < cycle.length - 1; i++) {
            const u = cycle[i];
            const v = cycle[i + 1];
            const edge = graph.edges.find(e =>
                (e.source.id === u && e.target.id === v) ||
                (e.source.id === v && e.target.id === u)
            );
            edges.filter(d => d === edge)
                .style("stroke", "red")
                .style("stroke-width", 4);
        }


        cycle.forEach(nodeId => {
            nodes.filter(d => d.id === nodeId)
                .style("fill", "orange");
        });

        await sleep(speed * 2);
    }


    async function resetCycle(cycle) {
        for (let i = 0; i < cycle.length - 1; i++) {
            const u = cycle[i];
            const v = cycle[i + 1];
            const edge = graph.edges.find(e =>
                (e.source.id === u && e.target.id === v) ||
                (e.source.id === v && e.target.id === u)
            );
            edges.filter(d => d === edge)
                .style("stroke", "black")
                .style("stroke-width", 2);
        }

        cycle.forEach(nodeId => {
            nodes.filter(d => d.id === nodeId)
                .style("fill", "lightblue");
        });

        await sleep(speed);
    }


    await dfs(startN, [], null);

    if (cycles.size > 0) {
        let cyclesText = `
        <div style="font-family: Arial, sans-serif; color: #333;">
            <h2 style="color: #d9534f; margin-bottom: 5px;">🔴 <strong>Ciclos detectados:</strong></h2>
            <div class="cycles-grid">
    `;

        let index = 1;
        cycles.forEach((cycle) => {
            cyclesText += `
            <div class="cycle-item">
                ${cycle}
            </div>
        `;
            index++;
        });

        cyclesText += `
            </div>
        </div>
    `;
        algorithmInfo.innerHTML = cyclesText;
    } else {
        algorithmInfo.innerHTML = `
        <div style="font-family: Arial, sans-serif; color: #333;">
            <h2 style="color: #5cb85c;">✅ <strong>No se detectaron ciclos.</strong></h2>
        </div>
    `;
    }
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
    } else if (algorithm === "bellman-ford") {
        bellmanFordStepByStep(startNodeId, speed);
    } else if (algorithm === "detect-cycles") {
        detectAndHighlightCycles(speed, startNodeId);
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
algorithmInfo.textContent = "Algoritmo de Prim: Encuentra el árbol de expansión mínima para un grafo no dirigido ponderado.";
document.getElementById("algorithm-select").addEventListener("change", () => {
    const algorithm = document.getElementById("algorithm-select").value;
    let info = "";
    if (algorithm === "prim") {
        info = "Algoritmo de Prim: Encuentra el árbol de expansión mínima para un grafo no dirigido ponderado.";
    } else if (algorithm === "kruskal") {
        info = "Algoritmo de Kruskal: Encuentra el árbol de expansión mínima para un grafo no dirigido ponderado.";
    } else if (algorithm === "dijkstra") {
        info = "Algoritmo de Dijkstra: Encuentra el camino más corto desde un nodo inicial a todos los demás nodos en un grafo ponderado.";
    } else if (algorithm === "bfs") {
        info = "Búsqueda en Anchura (BFS): Explora todos los nodos nivel por nivel desde un nodo inicial.";
    } else if (algorithm === "dfs") {
        info = "Búsqueda en Profundidad (DFS): Explora lo más lejos posible a lo largo de cada rama antes de retroceder.";
    } else if (algorithm === "bellman-ford") {
        info = "Algoritmo de Bellman-Ford: Encuentra el camino más corto desde un nodo inicial en un grafo dirigido con pesos negativos (sin ciclos negativos).";
    } else if (algorithm === "detect-cycles") {
        info = "Detección de ciclos: Detecta si un grafo dirigido contiene ciclos.";
    }
    algorithmInfo.textContent = info;
});