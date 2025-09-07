---
title: "Exercise 6: Deep Learning Visualization"
permalink: /2025-VisML-CSE/assignments/exercise6
author_profile: true
---

# Exercise 6: Deep Learning Visualization

**CS-GY 9223: Visualization for Machine Learning - Fall 2025**

**Released:** October 27, 2025  
**Due:** November 3, 2025 (11:59 PM EST)  
**Weight:** 8.33% of final grade

---

## Overview

Deep neural networks are complex, multi-layered systems that can be difficult to understand and debug. This assignment focuses on building comprehensive visualization tools for exploring neural network architectures, training dynamics, and learned representations. You will create interactive systems that make deep learning models more interpretable and debuggable.

## Learning Objectives

By completing this exercise, you will:
- Understand different approaches to visualizing neural network architectures
- Implement interactive tools for exploring layer activations and learned features
- Create visualizations for monitoring training dynamics and optimization
- Build tools for understanding attention mechanisms and model behavior
- Design interfaces that support deep learning model development and debugging

---

## Assignment Tasks

### Task 1: Network Architecture Visualization (30%)

Build comprehensive tools for visualizing neural network structures:

#### Interactive Network Diagrams
- **Layered Architecture Display:** Visual representation of network layers and connections
- **Parameter Information:** Show layer dimensions, parameter counts, and activation functions
- **Zoom and Navigation:** Detailed exploration of complex architectures (ResNet, Transformer, etc.)
- **Multiple View Types:** Node-link diagrams, block diagrams, and compact representations

#### Architecture Comparison Tool
- **Side-by-Side Comparison:** Compare different network architectures visually
- **Performance Overlay:** Show accuracy/loss metrics alongside architecture diagrams
- **Complexity Analysis:** Visualize computational complexity and memory requirements
- **Architecture Search:** Interactive exploration of architecture variants

#### Dynamic Architecture Exploration
- **Interactive Construction:** Build networks by adding/removing layers interactively
- **Real-time Validation:** Check architecture compatibility and compute requirements
- **Template Library:** Quick access to common architectures (VGG, ResNet, BERT, etc.)
- **Export Capabilities:** Generate code or config files from visual designs

### Task 2: Training Dynamics Visualization (25%)

Create tools for monitoring and understanding training processes:

#### Loss and Metrics Tracking
- **Multi-metric Dashboard:** Real-time plotting of loss, accuracy, and custom metrics
- **Training vs Validation:** Clear comparison of training and validation performance
- **Early Stopping Indicators:** Visual cues for overfitting and convergence
- **Smoothing and Filtering:** Options to reduce noise in training curves

#### Learning Rate and Optimization Analysis
- **Learning Rate Schedules:** Visualize learning rate changes throughout training
- **Gradient Analysis:** Plot gradient magnitudes and directions over time
- **Weight Evolution:** Show how specific weights change during training
- **Optimizer Comparison:** Compare different optimization algorithms side-by-side

#### Activation and Layer Analysis
- **Activation Distributions:** Histograms showing activation patterns per layer
- **Dead Neuron Detection:** Identify neurons that rarely activate
- **Layer Utilization:** Visualize which parts of the network are most active
- **Batch Normalization Effects:** Show distribution changes with/without batch norm

### Task 3: Feature and Representation Visualization (30%)

Implement tools for understanding what networks learn:

#### Convolutional Neural Network Analysis
- **Filter Visualization:** Display learned convolutional filters as images
- **Feature Maps:** Show intermediate layer outputs for specific inputs
- **Activation Maximization:** Generate images that maximally activate specific neurons
- **Saliency Maps:** Highlight input regions most important for predictions

#### Attention Mechanism Visualization
- **Attention Heatmaps:** Visual representation of attention weights
- **Multi-head Attention:** Separate visualization for different attention heads
- **Layer-wise Attention:** Show attention patterns at different network depths
- **Interactive Attention:** Explore attention for different input examples

#### Embedding and Representation Spaces
- **Hidden State Projections:** 2D/3D projections of high-dimensional hidden states
- **Word/Token Embeddings:** Interactive exploration of learned embeddings
- **Clustering Analysis:** Identify patterns in learned representations
- **Similarity Visualization:** Show relationships between different representations

### Task 4: Interactive Debugging Interface (15%)

Build tools to support deep learning model development:

#### Input Sensitivity Analysis
- **Perturbation Testing:** Show how small input changes affect outputs
- **Adversarial Example Generation:** Create and visualize adversarial inputs
- **Robustness Assessment:** Test model behavior under various input conditions
- **Feature Attribution:** Identify which input features drive specific predictions

#### Model Comparison and A/B Testing
- **Prediction Comparison:** Side-by-side prediction analysis for different models
- **Performance Profiling:** Compare speed, memory usage, and accuracy trade-offs
- **Error Analysis:** Deep dive into specific types of prediction errors
- **Statistical Testing:** Significance tests for model performance differences

---

## Technical Requirements

### Implementation Stack
- **D3.js v7+** for interactive visualizations and network diagrams
- **HTML5/CSS3** for responsive dashboard design
- **JavaScript ES6+** with modern async/await patterns
- **WebGL/Three.js** (optional) for 3D network visualization or complex animations

### Deep Learning Integration
Choose **one** of these approaches:
- **TensorFlow.js Integration:** Client-side model loading and inference
- **Python Backend:** Flask/FastAPI server with PyTorch/TensorFlow models
- **Pre-processed Data:** Work with saved activations, weights, and training logs
- **Mock Models:** Simplified networks for demonstration and educational purposes

### Recommended Libraries
- **TensorFlow.js:** Client-side deep learning model execution
- **PyTorch/TensorFlow:** Backend model training and analysis
- **Netron:** Reference for network architecture visualization patterns
- **TensorBoard:** Inspiration for training visualization layouts

---

## Required Features

### 1. Architecture Visualization System
```javascript
// Example network architecture structure
const networkArchitecture = {
    layers: [
        {
            name: "input",
            type: "input",
            shape: [224, 224, 3],
            parameters: 0
        },
        {
            name: "conv1",
            type: "conv2d",
            filters: 64,
            kernel_size: [3, 3],
            activation: "relu",
            parameters: 1792
        },
        {
            name: "pool1",
            type: "maxpool2d",
            pool_size: [2, 2],
            parameters: 0
        }
        // ... more layers
    ],
    connections: [
        {from: "input", to: "conv1"},
        {from: "conv1", to: "pool1"}
        // ... more connections
    ]
};
```

### 2. Training Visualization Dashboard
- **Real-time Metrics:** Live updating charts during training
- **Historical Analysis:** Explore training history with zoom and pan
- **Comparative View:** Multiple training runs on same plot
- **Export Functions:** Save training curves and analysis results

### 3. Feature Exploration Interface
- **Layer Selection:** Choose which layer to visualize
- **Input Sample Browser:** Select from dataset samples for analysis
- **Filter/Feature Grid:** Display multiple features/filters simultaneously
- **Interactive Controls:** Adjust visualization parameters in real-time

---

## Datasets and Models

Choose **two** of these scenarios for comprehensive demonstration:

### 1. Computer Vision: CIFAR-10 Classification
- **Model Type:** Convolutional Neural Network (CNN)
- **Architecture:** Custom CNN or ResNet variant
- **Visualization Focus:** Convolutional filters, feature maps, saliency analysis
- **Training Data:** Include training logs with loss/accuracy over epochs

### 2. Natural Language Processing: Text Classification
- **Model Type:** Transformer or LSTM-based model
- **Architecture:** BERT-like or custom sequence model
- **Visualization Focus:** Attention mechanisms, embedding spaces, token importance
- **Training Data:** Training dynamics and attention pattern evolution

### 3. Time Series: Stock Price or Weather Prediction
- **Model Type:** LSTM, GRU, or Transformer for sequences
- **Architecture:** Multi-layer recurrent or attention-based network
- **Visualization Focus:** Hidden state evolution, temporal attention patterns
- **Training Data:** Sequence learning dynamics and prediction quality

### 4. Generative Model: VAE or Simple GAN
- **Model Type:** Variational Autoencoder or Generative Adversarial Network
- **Architecture:** Encoder-decoder or generator-discriminator structure
- **Visualization Focus:** Latent space exploration, generation process
- **Training Data:** Generative training dynamics, loss curves for multiple components

---

## Deliverables

### 1. Interactive Deep Learning Visualization System
Deploy a comprehensive tool featuring:
- **Network architecture explorer** with multiple visualization modes
- **Training dynamics dashboard** with real-time and historical analysis
- **Feature visualization suite** for understanding learned representations
- **Interactive debugging tools** for model development support

### 2. Technical Report (5-6 pages)
Submit a comprehensive analysis covering:

**Introduction and Motivation (0.5 pages)**
- Importance of visualization in deep learning development
- Overview of implemented visualization techniques and their applications
- Related work in neural network visualization tools

**System Architecture and Implementation (2 pages)**
- Technical architecture of the visualization system
- Integration approach with deep learning frameworks
- Performance optimization strategies for real-time visualization
- User interface design principles and interaction patterns

**Deep Learning Analysis and Case Studies (2 pages)**
- Detailed analysis of chosen model scenarios using the visualization system
- Insights discovered through architecture and training visualization
- Feature analysis and interpretation of learned representations
- Debugging examples where visualization helped identify issues

**Evaluation and User Experience (1 page)**
- Usability evaluation of the visualization interface
- Performance analysis with different model sizes and complexities
- Comparison with existing tools (TensorBoard, Netron, etc.)
- User feedback and iteration based on testing

**Future Enhancements and Conclusions (0.5 pages)**
- Limitations of current implementation and areas for improvement
- Potential extensions for different types of neural networks
- Integration possibilities with ML development workflows

### 3. Code Repository and Documentation
Create a comprehensive repository including:
- **Complete source code** with modular, documented architecture
- **Model integration examples** for different deep learning frameworks
- **Setup and deployment instructions** for reproducing the system
- **User manual** with guidance for interpreting visualizations
- **Live demo** with pre-loaded models and datasets

---

## Evaluation Criteria

### Technical Implementation (25%)
- **Framework Integration:** Effective connection with deep learning models
- **Visualization Quality:** Accurate and informative representation of network components
- **Performance:** Smooth interactions with complex models and large datasets
- **Code Architecture:** Clean, modular, well-documented implementation

### Deep Learning Understanding (25%)
- **Domain Knowledge:** Accurate representation of deep learning concepts
- **Feature Analysis:** Meaningful interpretation of learned representations
- **Training Insights:** Valuable analysis of optimization and learning dynamics
- **Model Debugging:** Practical tools for identifying and resolving issues

### Visualization Design (20%)
- **Information Design:** Effective encoding of complex neural network information
- **Interactive Experience:** Intuitive controls and responsive feedback
- **Multiple Views:** Coordinated multiple perspectives on the same model
- **Scalability:** Handling of different model sizes and architectures

### Analysis and Insights (20%)
- **Case Study Depth:** Thorough exploration of chosen deep learning scenarios
- **Comparative Analysis:** Meaningful comparison between different approaches
- **Novel Discoveries:** Insights gained through visualization that weren't obvious otherwise
- **Practical Value:** Tools and insights useful for actual deep learning development

### Communication and Documentation (10%)
- **Report Clarity:** Professional technical writing with clear explanations
- **Code Documentation:** Comprehensive documentation for system usage and extension
- **User Experience:** Clear guidance for interpreting and using visualizations
- **Reproducibility:** Complete instructions for setup and replication

---

## Bonus Opportunities (+10% each, max +20%)

### Advanced Visualization Techniques
- **3D Network Visualization:** Interactive 3D representation of deep architectures
- **Animation and Transitions:** Smooth animated transitions showing network evolution
- **VR/AR Interface:** Immersive exploration of neural network structures

### Specialized Deep Learning Applications
- **Graph Neural Networks:** Visualization tools for GNN architectures and node representations
- **Reinforcement Learning:** Action-value function visualization and policy analysis
- **Neural Architecture Search:** Interactive exploration of automated architecture search

### Integration and Deployment
- **Real-time Training Integration:** Live connection to training processes for real-time visualization
- **Collaborative Features:** Share visualizations and insights with team members
- **Cloud Deployment:** Scalable deployment for analyzing large production models

---

## Submission Instructions

1. **Deploy Visualization System:** Host complete application online (AWS, Google Cloud, Heroku, etc.)
2. **Create Repository:** Name it `visml-exercise6-[username]`
3. **Prepare Submission Package:**
   - Live system URL with demo models and datasets
   - GitHub repository link with complete source code
   - Technical report (PDF format)
   - 7-10 minute video demonstration showcasing key features and insights
4. **Submit via NYU Classes:** Upload all materials and provide access links

**Late Policy:** 20% deduction per day, maximum 5 days late

---

## Resources

### Deep Learning Visualization Literature
- Zeiler & Fergus, "Visualizing and Understanding Convolutional Networks" (2014)
- Yosinski et al., "Understanding Neural Networks Through Deep Visualization" (2015)
- Olah et al., "The Building Blocks of Interpretability" (Distill, 2018)
- Hohman et al., "Visual Analytics in Deep Learning: An Interrogative Survey" (2018)

### Technical Implementation Resources
- [TensorFlow.js Documentation](https://www.tensorflow.org/js)
- [PyTorch Visualization Tutorial](https://pytorch.org/tutorials/intermediate/tensorboard_tutorial.html)
- [Netron Neural Network Viewer](https://github.com/lutzroeder/netron)
- [TensorBoard Visualization Toolkit](https://www.tensorflow.org/tensorboard)

### Visualization Inspiration
- [Distill Neural Network Articles](https://distill.pub/)
- [ConvNetJS Demos](https://cs.stanford.edu/people/karpathy/convnetjs/)
- [TensorSpace.js](https://github.com/tensorspace-team/tensorspace)
- [CNN Explainer](https://poloclub.github.io/cnn-explainer/)

### Architecture Analysis Tools
- [Netron Model Visualizer](https://netron.app/)
- [TensorBoard Graph Dashboard](https://www.tensorflow.org/tensorboard/graphs)
- [Weights & Biases Model Visualization](https://docs.wandb.ai/guides/models)

---

## Example Code Structure

### Network Architecture Visualization
```javascript
class NetworkArchitectureVisualizer {
    constructor(container) {
        this.container = container;
        this.svg = d3.select(container).append('svg');
        this.setupZoomAndPan();
    }
    
    renderNetwork(architecture) {
        // Create layer nodes
        const layers = this.svg.selectAll('.layer')
            .data(architecture.layers)
            .enter()
            .append('g')
            .attr('class', 'layer');
            
        // Add connections between layers
        const connections = this.svg.selectAll('.connection')
            .data(architecture.connections)
            .enter()
            .append('line')
            .attr('class', 'connection');
            
        // Position layers and connections
        this.updateLayout();
    }
    
    highlightActivePath(inputData) {
        // Show data flow through network
        this.animateActivation(inputData);
    }
}
```

### Training Visualization Dashboard
```javascript
class TrainingDashboard {
    constructor(container) {
        this.container = container;
        this.setupCharts();
        this.metrics = {
            loss: [],
            accuracy: [],
            learning_rate: []
        };
    }
    
    updateMetrics(epoch, newMetrics) {
        // Add new data point
        this.metrics.loss.push({epoch, value: newMetrics.loss});
        this.metrics.accuracy.push({epoch, value: newMetrics.accuracy});
        
        // Update visualizations
        this.updateLossChart();
        this.updateAccuracyChart();
        this.updateLearningRateChart();
    }
    
    setupRealTimeUpdates(trainingProcess) {
        // Connect to training process for live updates
        trainingProcess.onEpochComplete((metrics) => {
            this.updateMetrics(metrics.epoch, metrics);
        });
    }
}
```

---

## Getting Help

- **Discord Support:** Use #exercise6 channel for questions and technical discussions
- **Deep Learning Concepts:** Office hours available for neural network architecture questions
- **Framework Integration:** TA support for connecting visualization to ML frameworks
- **Performance Optimization:** Help with optimizing visualization performance for large models
- **Visualization Design:** Feedback on effective deep learning visualization approaches

---

## Academic Integrity

- **Individual Work:** Complete this assignment independently
- **Framework Attribution:** Properly credit any deep learning frameworks and pre-trained models used
- **Code Attribution:** Cite external visualization libraries and code examples
- **Model Usage:** Clearly indicate whether models are self-trained or obtained from external sources
- **Original Analysis:** Your insights and visualization design must be original work

---

*Questions? Post in Discord #exercise6 channel or contact the teaching team.*