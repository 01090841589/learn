const VueLoaderPlugin = require('vue-loader/lib/plugin')
const path = require('path')


module.exports = {
  mode: 'development',
  entry: {
    app: path.join(__dirname, 'src', 'main.js')
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        use: 'vue-loader',
      },
      {
        test: /\.css$/,
        use: ['vue-style-loader', 'css-loader']
      }
    ]
  },
  plugins: [
    new VueLoaderPlugin(),
  ],
  output: {
    filename: 'app.js',
    path: path.join(__dirname, 'dist')
  },
}