const marked = require('marked');
const chalk = require('chalk');
const path = require('path');
const fs = require('fs');

const config = require('../config/default');     

class DocumentationGenerator {
    /**
     * The DocumentationGenerator object is responsible for converting each
     * markdown file listed in this project into an html file for the React
     * website.
     */

    constructor() {
        /** Figure I/O */

        this.out_dir = path.join(
            config.rootDir, 'public/documentation'
        );
        this.files = [{
            name: "main",
            input: path.join(config.rootDir, 'README.md'),
            output: `${this.out_dir}\\main.html`
        }];
    }

    generate = () => {
        /** Generate documentation */

        // Wrapper tags (for styling the html)
        const docTags = [
            '<div class="documentation">',
            '</div>'
        ]

        for (let i=0; i<this.files.length; i++) {
            console.log(
                chalk.blue(`Generating ${this.files[i].output} documentation...`)
            );

            // Convert markdown to HTML
            let markdown, html;
            try {   
                markdown = fs.readFileSync(this.files[i].input, 'utf-8');
                html = `${docTags[0]}${marked(markdown)}${docTags[1]}`;
            } catch(e) {
                console.log(
                    chalk.red(`Error reading markdown for ${this.files[i].output}`)
                );
            }

            // Create HTML file
            try {
                fs.writeFile(this.files[i].output, html, (err) => {
                    if (err) throw err;
                    console.log(
                        chalk.blue(
                            `Documentation for ${this.files[i].output} generated.`
                        )
                    );
                });
            } catch(e) {
                console.log(
                    chalk.red(
                        `Error writing markdown for ${this.files[i].output}`
                    ), e
                );
            }
        }

        console.log(chalk.green('Finished generating documentation.'));
        return;
    }
}

module.exports = DocumentationGenerator;