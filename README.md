# LPC-Based Voice Anonymization

## Overview

This project focuses on the development and implementation of an LPC (Linear Predictive Coding)-based method for voice anonymization. It aims to anonymize speech signals to degrade the reliability of automatic approaches to speaker recognition while preserving the intelligibility and naturalness of speech. This method involves altering the speaker's voice characteristics along with linguistic content and extralinguistic traits to prevent identification, ensuring privacy in voice-activated interfaces.

## Team Members

- Arkadiy Aliev
- Vsevolod Ivanov
- Yuriy Ivanov
- Mikhail Mishustin
- Andrey Safronov

## Installation

### Prerequisites

- Python 3.6 or higher
- NumPy
- SciPy
- Any additional dependencies are listed in `requirements.txt`.

### Setup

1. Clone the repository:

```bash
git clone https://github.com/ArkadiyAliev/LPC-based-voice-anonymisation.git
```

2. Install the required Python packages:

```bash
cd LPC-based-voice-anonymisation
pip install -r requirements.txt
```

## Usage

To use the LPC-based voice anonymization method, follow the instructions below:

1. Prepare your audio files in a supported format (e.g., WAV).

2. Run the main script with the path to your audio file:

```bash
python anonymize.py --input <path_to_your_audio.wav>
```

3. The anonymized audio will be saved in the specified output directory.

## Methodology

This project employs LPC for encoding speech signals, transforming LPC coefficients, and decoding them to achieve anonymization. It compares this approach with other existing models for quality of anonymization and preservation of speech meaning. Key aspects include:

- The use of the McAdams coefficient for shifting pole positions derived from LPC analysis.
- Comparison with neural network-based methods and traditional signal processing techniques.
- Evaluation based on anonymity and speech intelligibility, using metrics like Cosine Similarity and Word Error Rate (WER).

## Experiments

The experiments were conducted using the Common Voice dataset, focusing on the anonymization quality and the impact on speech intelligibility. Detailed results, including comparisons of time efficiency and memory usage between LPC and neural network-based methods, are documented in the final project report.

## Acknowledgments

This project was conducted as part of the Machine Learning 2023 Course at Skoltech, Moscow, Russian Federation.
