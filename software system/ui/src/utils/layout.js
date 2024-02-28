export function forceDirectedLayout(nodes, links, width, height, iterations) {
  let positions = {};
  nodes.forEach(node => {
    positions[node.id] = {
      x: Math.random() * width,
      y: Math.random() * height
    };
  });
  let k = Math.sqrt(width * height / nodes.length);
  let alpha = 0.1;

  for (let i = 0; i < iterations; i++) {
    nodes.forEach(node => {
      let { x, y } = positions[node.id];
      let forceX = 0;
      let forceY = 0;

      nodes.forEach(otherNode => {
        if (node.id !== otherNode.id) {
          let dx = x - positions[otherNode.id].x;
          let dy = y - positions[otherNode.id].y;
          let distance = Math.sqrt(dx * dx + dy * dy);
          forceX += dx / distance * k * k / distance;
          forceY += dy / distance * k * k / distance;
        }
      });
      links.forEach(link => {
        if (link.source === node.id) {
          let dx = x - positions[link.target].x;
          let dy = y - positions[link.target].y;
          forceX -= dx * k;
          forceY -= dy * k;
        } else if (link.target === node.id) {
          let dx = x - positions[link.source].x;
          let dy = y - positions[link.source].y;
          forceX += dx * k;
          forceY += dy * k;
        }
      });

      positions[node.id].x += forceX * alpha;
      positions[node.id].y += forceY * alpha;

      positions[node.id].x = Math.max(0, Math.min(width, positions[node.id].x));
      positions[node.id].y = Math.max(0, Math.min(height, positions[node.id].y));
    });

    alpha *= 0.99;
  }

  return {
    nodes: nodes.map(node => {
      return {
        ...node,
        x: positions[node.id].x,
        y: positions[node.id].y
      };
    }),
  }
}